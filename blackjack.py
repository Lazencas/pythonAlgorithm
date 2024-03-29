# 문제
# 카지노에서 제일 인기 있는 게임 블랙잭의 규칙은 상당히 쉽다. 
# 카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임이다. 블랙잭은 카지노마다 다양한 규정이 있다.
# 한국 최고의 블랙잭 고수 김정인은 새로운 블랙잭 규칙을 만들어 상근, 창영이와 게임하려고 한다.
# 김정인 버전의 블랙잭에서 각 카드에는 양의 정수가 쓰여 있다.
#  그 다음, 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다. 그런 후에 딜러는 숫자 M을 크게 외친다.
# 이제 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다. 블랙잭 변형 게임이기 때문에, 
# 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.
# N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.

# 입력
# 첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 
# 이 값은 100,000을 넘지 않는 양의 정수이다.

# 합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.

# 출력
# 첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.

#각 카드에는 양의 정수, N장의 카드를 바닥에 놓고, 딜러는 숫자 M을 외침, N장의 카드중에 3장의 카드 고름, M을 넘지 않고 M과
#최대한 가깝게

#cardnum은 카드 개수이고 여기서 3개뽑아서 obnum에 가장 가까운 숫자를 만들어야함
#card_list를 일단 모든 경우의 수 대로 숫자 뽑고 3중반복문
#obnum에 가까운지 체크하는 법 -> obnum보다 작거나 같고, 정답에 들어있는 숫자보다 크면 정답 교체 
cardnum, obnum = map(int,input().split(' '))
card_list = list(map(int,input().split(' ')))
temp_list = card_list

answer = 0
temp_answer = 0

for i in range(0, len(temp_list)):

    for j in range(i+1, len(temp_list)):

        for k in range(j+1, len(temp_list)):

            temp_answer = temp_list[i]+temp_list[j]+temp_list[k]

            if temp_answer<=obnum and temp_answer>answer:
                answer = temp_answer

print(answer)





