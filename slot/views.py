from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import PlayerScore
import random
import json

def landing(request):
    return render(request, 'landing.html')

def slot_game(request):
    # Get or create player score
    player_score, created = PlayerScore.objects.get_or_create(
        player_name='Anonymous',
        defaults={'score': 1000}
    )
    return render(request, 'slot.html', {'initial_balance': player_score.score})

def spin(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            current_balance = data.get('balance', 0)
            bet_amount = 10
            
            if current_balance < bet_amount:
                return JsonResponse({
                    'error': 'Insufficient balance',
                    'balance': current_balance
                })
            
            symbols = ['🍒', '🍊', '🍋', '🍇', '💎', '7']
            result = [random.choice(symbols) for _ in range(3)]
            
            # Check for win
            if len(set(result)) == 1:  # All symbols match
                if result[0] == '7':
                    win_amount = 1000
                    message = "JACKPOT! You won $1000!"
                elif result[0] == '💎':
                    win_amount = 500
                    message = "Big Win! You won $500!"
                else:
                    win_amount = 100
                    message = f"You won $100!"
            else:
                win_amount = 0
                message = "Try again!"
            
            # Update balance
            new_balance = current_balance - bet_amount + win_amount
            
            # Update player score in database
            player_score = PlayerScore.objects.get(player_name='Anonymous')
            player_score.score = new_balance
            player_score.save()
            
            return JsonResponse({
                'result': result,
                'message': message,
                'win_amount': win_amount,
                'balance': new_balance
            })
            
        except Exception as e:
            return JsonResponse({
                'error': str(e),
                'balance': current_balance
            })
    
    return JsonResponse({'error': 'Invalid request method'})
