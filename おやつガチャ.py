import random

# 市販のおやつデータ（40種類）
# 各おやつ：[名前, ジャンル, 概算価格, 気分タグ]
SNACKS = [
    # --- グミ (5種) ---
    {"name": "果汁グミ (明治)", "genre": "グミ", "price": 140, "mood": "フルーティー"},
    {"name": "ピュレグミ (カンロ)", "genre": "グミ", "price": 150, "mood": "甘酸っぱい"},
    {"name": "タフグミ (カバヤ)", "genre": "グミ", "price": 200, "mood": "ガッツリ"},
    {"name": "ハリボー ゴールドベア", "genre": "グミ", "price": 230, "mood": "噛みごたえ"},
    {"name": "忍者めし (UHA味覚糖)", "genre": "グミ", "price": 130, "mood": "噛みごたえ"},

    # --- ポテチ・スナック (10種) ---
    {"name": "カルビー ポテトチップス うすしお", "genre": "ポテチ", "price": 160, "mood": "定番・しょっぱい"},
    {"name": "堅あげポテト (カルビー)", "genre": "ポテチ", "price": 180, "mood": "ザクザク・しょっぱい"},
    {"name": "ピザポテト (カルビー)", "genre": "ポテチ", "price": 180, "mood": "濃厚・ガッツリ"},
    {"name": "湖池屋 ストロング", "genre": "ポテチ", "price": 170, "mood": "ガッツリ・濃厚"},
    {"name": "チップスター (ヤマザキ)", "genre": "ポテチ", "price": 140, "mood": "サクサク"},
    {"name": "うまい棒 (1本)", "genre": "スナック", "price": 15, "mood": "お手軽・しょっぱい"},
    {"name": "じゃがりこ サラダ (カルビー)", "genre": "スナック", "price": 170, "mood": "ザクザク"},
    {"name": "キャベツ太郎 (菓道)", "genre": "スナック", "price": 40, "mood": "お手軽・濃厚"},
    {"name": "かっぱえびせん (カルビー)", "genre": "スナック", "price": 150, "mood": "定番・サクサク"},
    {"name": "エアリアル (ヤマザキ)", "genre": "スナック", "price": 150, "mood": "サクサク・濃厚"},

    # --- チョコレート (10種) ---
    {"name": "ブラックサンダー (有楽製菓)", "genre": "チョコ", "price": 50, "mood": "お手軽・ガッツリ"},
    {"name": "アルフォート (ブルボン)", "genre": "チョコ", "price": 130, "mood": "サクサク・甘い"},
    {"name": "ポッキー (江崎グリコ)", "genre": "チョコ", "price": 180, "mood": "定番・甘い"},
    {"name": "キットカット (ネスレ)", "genre": "チョコ", "price": 200, "mood": "甘い・シェア"},
    {"name": "きのこの山 (明治)", "genre": "チョコ", "price": 230, "mood": "甘い・サクサク"},
    {"name": "たけのこの里 (明治)", "genre": "チョコ", "price": 230, "mood": "甘い・ザクザク"},
    {"name": "ガルボ (明治)", "genre": "チョコ", "price": 160, "mood": "濃厚・しっとり"},
    {"name": "チロルチョコ (1個)", "genre": "チョコ", "price": 30, "mood": "お手軽・甘い"},
    {"name": "アポロ (明治)", "genre": "チョコ", "price": 140, "mood": "フルーティー・甘い"},
    {"name": "メルティーキッス (明治)", "genre": "チョコ", "price": 280, "mood": "贅沢・濃厚"},

    # --- クッキー・ビスケット (8種) ---
    {"name": "カントリーマアム (不二家)", "genre": "クッキー", "price": 250, "mood": "しっとり・甘い"},
    {"name": "オレオ (ナビスコ)", "genre": "クッキー", "price": 220, "mood": "ザクザク・甘い"},
    {"name": "マリー (森永)", "genre": "ビスケット", "price": 180, "mood": "素朴・あっさり"},
    {"name": "ムーンライト (森永)", "genre": "ビスケット", "price": 180, "mood": "サクサク・甘い"},
    {"name": "チョイス (森永)", "genre": "ビスケット", "price": 180, "mood": "サクサク・素朴"},
    {"name": "たべっ子どうぶつ (ギンビス)", "genre": "ビスケット", "price": 140, "mood": "素朴・サクサク"},
    {"name": "パイの実 (ロッテ)", "genre": "ビスケット", "price": 180, "mood": "サクサク・甘い"},
    {"name": "源氏パイ (三立製菓)", "genre": "パイ", "price": 200, "mood": "サクサク・甘い"},

    # --- 和菓子・せんべい・その他 (7種) ---
    {"name": "ハッピーターン (亀田製菓)", "genre": "せんべい", "price": 180, "mood": "定番・甘じょっぱい"},
    {"name": "柿の種 (亀田製菓)", "genre": "せんべい", "price": 200, "mood": "おつまみ・ピリ辛"},
    {"name": "ばかうけ (栗山米菓)", "genre": "せんべい", "price": 180, "mood": "定番・しょっぱい"},
    {"name": "雪の宿 (三幸製菓)", "genre": "せんべい", "price": 180, "mood": "甘じょっぱい・サクサク"},
    {"name": "チョコバット (三立製菓)", "genre": "駄菓子", "price": 40, "mood": "お手軽・甘い"},
    {"name": "おやつカルパス (プリマハム)", "genre": "珍味", "price": 15, "mood": "お手軽・おつまみ"},
    {"name": "ビッグカツ (菓道)", "genre": "駄菓子", "price": 40, "mood": "お手軽・ガッツリ"}
]


def snack_gacha():
    print("=== 🍪 おやつガチャ 🍪 ===")
    
    try:
        max_budget = int(input("上限予算を入力してください（例: 50, 150, 300）: "))
    except ValueError:
        print("数字を入力してください。")
        return

    print("\n【今の気分を選んでください】")
    print("1: 甘いものが食べたい（チョコ、クッキー）")
    print("2: しょっぱい・ガッツリ食べたい（ポテチ、スナック、せんべい）")
    print("3: 歯ごたえが欲しい・リフレッシュ（グミ）")
    print("4: なんでもOK（完全おまかせ）")
    
    mood_choice = input("選択肢 (1-4): ")

    filtered_snacks = []
    
    for snack in SNACKS:
        if snack["price"] <= max_budget:
            if mood_choice == "1" and snack["genre"] in ["チョコ", "クッキー", "ビスケット", "パイ"]:
                filtered_snacks.append(snack)
            elif mood_choice == "2" and snack["genre"] in ["ポテチ", "スナック", "せんべい", "駄菓子", "珍味"]:
                filtered_snacks.append(snack)
            elif mood_choice == "3" and snack["genre"] in ["グミ"]:
                filtered_snacks.append(snack)
            elif mood_choice == "4":
                filtered_snacks.append(snack)

    # 該当結果の出力
    if not filtered_snacks:
        print(f"\n残念！ {max_budget}円以下でその条件に合うおやつは見つかりませんでした...")
    else:
        result = random.choice(filtered_snacks)
        print("\n-------------------------")
        print("🎉 ガチャ結果！今日のおやつはこれ！ ")
        print(f"商品名 : {result['name']}")
        print(f"ジャンル: {result['genre']}")
        print(f"目安価格: 約{result['price']}円")
        print(f"特徴    : {result['mood']}")
        print("-------------------------")


if __name__ == "__main__":
    snack_gacha()