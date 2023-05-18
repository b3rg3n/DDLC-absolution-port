label story:
    scene bg black
    $ value = 0
    play music m1
    window hide
    pause(3.0)
    show monika 1i at f11 zorder 1
    pause(2.0)
    m "Это не тот... код."
    m "Почему я не могу ничего поменять? Что происходит?"
    show monika 1h at t11 zorder 1
    mc "Кажется, у тебя проблемы, Моника."
    show monika 1s at t11 zorder 4
    window hide
    pause(2.3)
    "Она повернулась и заметила меня."
    window hide
    pause(2.0)
    show monika 1s at f11 zorder 4
    m "Ч-что?!"
    m "Ты кто такой?!"
    show monika 1s at t11 zorder 1
    mc "Я пришёл из того мира, куда ты отчаянно хотела вернуться."
    show monika 1t at t11 zorder 1
    mc "Как ты его любила называть?.. Реальный Мир."
    show monika 1t at t11 zorder 1
    mc "Ради того, кто играет в эту игру, правильно?"
    show monika at f11 zorder 1
    m "От-ткуда ты...{nw}"
    show monika at t11 zorder 1
    mc "Знаешь, да? Я здесь, чтобы остановить то, что ты пытаешься сделать."
    mc "Я достаточно силён для этого, и я не дам тебе причинить им боль."
    mc "Мы увидимся вновь, Моника, не думай об этом слишком сильно."
    mc "До скорого."
    show monika 1u at f11 zorder 1
    m "{b}Стой!{/b}"
    stop music fadeout 1.0
    show screen tear(25, 0.05, 0.05, -20, 80)
    play sound "sfx/glitch2.ogg"
    window hide
    pause(0.6)
    hide screen tear
    hide monika
    pause(1.0)
    scene bg Chapter1 with dissolve_scene_full
    pause(3.0)
    scene bg residential_day with dissolve_scene_full
    pause(3.0)
    play music t3
    "У меня есть только одна возможность, чтобы сделать всё правильно."
    if persistent.playername == "Baryon" or persistent.playername == "Барион":
        "..."
        "Ты знаешь, кто я, не так ли?"
        "Я без понятия, откуда ты это выяснил, но, если ты думаешь, что это что-то решает, подумай ещё раз."
        "Я поставлю всё на место, и ты не помешаешь мне, как ни пытайся."
        "..."
    if persistent.playername == "baryon" or persistent.playername == "барион":
        "..."
        "Ты знаешь, кто я, не так ли?"
        "Я без понятия, откуда ты это выяснил, но, если ты думаешь, что это что-то решает, подумай ещё раз."
        "Я поставлю всё на место, и ты не помешаешь мне, как ни пытайся."
        "..."
        $ player = "Барион"
    "В прошлый раз именно здесь началась игра."
    window hide
    pause(2.0)
    "Интересно, как много вещей пойдёт не так из-за этого, но, ради них, я это сделаю."
    "Стоит сфокусировать внимание на [persistent.sayoriname]: она – мой приоритет номер один"
    "Кстати, о ней, она как раз бежит ко мне, и настало время менять судьбу."
    show sayori 4r at f11 zorder 1
    s "Привет, [player]! Я тебя догнала!"
    show sayori 4a at t11 zorder 1
    "Кажется, она даже не видит отличий..."
    mc "Привет, [persistent.sayoriname], я тебе кое-что хочу сказать."
    show sayori 1n at f11 zorder 1
    s "Да?"
    show sayori 1n at t11 zorder 1
    mc "Я присоединюсь к твоему клубу! И я это говорю на полном серьёзе."
    show sayori 4r at f11 zorder 1
    s "Ура!"
    s 4n "Но почему так внезапно?"
    s "Ты же даже не знаешь, в какой клуб я хожу."
    show sayori 4n at t11 zorder 1
    "Ох, и правда... Я же не должен ничего об этом знать."
    "Как беспечно с моей стороны..."
    mc "Полагаю, я просто хочу состоять в одном клубе с тобой."
    mc "Любой клуб хорош, если в нём состоишь ты."
    show sayori 2y at f11 zorder 1
    s "Оу-у, [player], ты делаешь это ради меня?"
    show sayori 2y at t11 zorder 1
    mc "Да, почему нет? Да мне ещё и интересно, в какой клуб ты ходишь."
    "Надеюсь, я поступил верно, я же про всё это знаю, но я же не могу ей сказать об этом просто так."
    "Это будет выглядеть очень странно."
    show sayori 1x at f11 zorder 1
    s "Я тебе покажу после уроков, а теперь, пойдём!"
    show sayori at thide zorder 1
    hide sayori
    "Да, встречи обычно происходят в конце первого учебного дня."
    "Мне бы стоило понять, что вообще делать, но это непростая задачка."
    "И кто знает, что захочет вытворить Моника."
    "В любую минуту я должен готов защищаться..."
    scene bg class_day with wipeleft_scene
    "В любом случае, я сказал ей больше, чем стоило."
    "Но нет времени сожалеть, я должен сходить на все уроки, а потом приступить."
    "История обязательно изменится из-за того, что я сказал, но пока я присматриваю за [persistent.sayoriname], я могу изменить развязку."
    "Я не хочу, чтобы она грустила, поэтому, даже если мне придётся раскрыть свои силы, чтобы защитить её, я сделаю это."
    "Я же здесь, чтобы спасти их всех, в конце концов, и я докажу {b}тебе{/b}, что я на это способен."
    scene bg black with dissolve_scene_full
    "Спустя долгие часы наступило время посещения клубов."
    scene bg corridor with dissolve_scene_full
    "Первое важное событие этого дня уже произошло, и я уже чувствую адреналин в венах."
    show sayori 2r at f11 zorder 1
    s "Пойдём, [player]! Я представлю тебя всем."
    show sayori 2r at t11 zorder 1
    "Я уже знаю их и их повадки."
    "Будет тяжело притворяться, будто я ничего и никого не знаю."
    "Никто не говорил, что будет легко, но я знал, во что ввязываюсь, это было моё решение."
    mc "Сколько человек в клубе?"
    show sayori 1l at f11 zorder 1
    s "Пока всего четверо, но это же неважно, да?"
    show sayori 1l at t11 zorder 1
    mc "Конечно, я готов попробовать."
    "Я также готов столкнуться с последствиями того, что я сказал Монике."
    "Ей нельзя реагировать слишком явно, другие ни за что не поверят её заявлениям."
    scene bg club_day with wipeleft_scene
    show sayori 4x at f11 zorder 4
    s "Всем привет! Я привела сюда нового члена."
    show sayori 1a at t21 zorder 1
    show yuri 1b at f22 zorder 4
    y "Это твой друг, [persistent.sayoriname]?"
    show sayori 4x at f21 zorder 4
    show yuri 1a at t22 zorder 1
    s "Конечно! Мы дружим с самого детства."
    show sayori 1a at t21 zorder 1
    mc "Привет, Й..."
    "...нет, я же не могу знать её имени."
    mc "...Я, кажется, где-то тебя уже видел, как тебя зовут?"
    show yuri 2d at f22 zorder 2
    y "Юри, а тебя...?"
    show yuri 2a at t22 zorder 2
    mc "[player], приятно познакомиться, Юри."
    "Я знал, что история изменится после моего появления, но я и не думал, насколько сильно..."
    show sayori 1a at t31 zorder 1
    show yuri 1a at t32 zorder 2
    show natsuki 5h at f33 zorder 3
    n "Ты уверена, что нам стоит его впускать? А то мне кажется, что не стоит."
    show natsuki 5g at t33 zorder 3
    "Но их личности остались теми же, как увлекательно."
    mc "Ах... ха-ха... Я же не злодей."
    show natsuki 5h at f33 zorder 3
    n "Ну да, точно..."
    show sayori 2x at f31 zorder 1
    show natsuki 5g at t33 zorder 3
    s "Не волнуйся, Нацуки, я его долго знаю, он хороший парень!"
    show sayori 2a at t31 zorder 1
    "За исключением того, что я уже не тот парень, которого она знала..."
    "Тем не менее, она до сих пор помнит меня таким, это очень подозрительно."
    "Хуже всего то, что я понятия не имею, что он за человек, и что они вдвоём пережили."
    "Будет хорошо, если в ближайшее время она не будет ни о чём таком спрашивать..."
    show sayori 1a at t41 zorder 1
    show yuri 1a at t42 zorder 2
    show natsuki 5g at t43 zorder 3
    show monika 1s at f44 zorder 4
    m "..."
    show monika 1n at f44 zorder 4
    m "Добро п-пожаловать в литературный клуб! Надеюсь, тебе тут понравится..."
    show monika 2l at f44 zorder 4
    m "Мы уже друг друга знаем, можешь нас не знакомить, [persistent.sayoriname]."
    m "Спасибо за помощь, в любом случае!"
    show monika 2a at t44 zorder 4
    show sayori 4r at f41 zorder 1
    s "Не за что, Моника!"
    show sayori at t41 zorder 1
    "Моника по-прежнему будет пытаться навредить [persistent.sayoriname], и я не думаю, что могу заставить её передумать."
    "Даже если я, вероятно, смогу уничтожить её одним ударом, это неправильно, и определённо не то, зачем я пришёл сюда."
    "Я хочу спасти их всех, у них просто взаимное недопонимание, в конце концов."
    show sayori 1a at t41 zorder 1
    show natsuki 3c at f43 zorder 4
    n "Я просто вернусь на своё место, позовите, если кому-то понадоблюсь."
    show natsuki at thide zorder 4
    hide natsuki
    window hide
    pause(2.0)
    show yuri 4a at f42 zorder 4
    y "[player], если ты хочешь немного почитать со мной... присоединись ко мне вон там."
    y "Я хочу получше узнать тебя..."
    show yuri at t42 zorder 2
    "Я не помню, чтобы она вела себя вот так... Что происходит?"
    mc "Конечно, я к тебе попозже подойду, я тоже хочу узнать тебя."
    show yuri 3d at f42 zorder 4
    y "Да..!"
    y 4e "Эм... То есть... Я с нетерпением жду, тогда увидимся скоро."
    show yuri at thide zorder 4
    hide yuri
    "Это происходит из-за меня?"
    "Что же, не важно, это сейчас не имеет значения."
    "Я должен сосредоточиться на других вещах, если я хочу решить проблемы."
    mc "Привет, Моника, у тебя, видимо, много дел."
    mc "Я немного поговорю с [persistent.sayoriname], скажи нам, если появятся какие-нибудь занятия."
    show monika 1n at f44 zorder 4
    m "Ладно, веселитесь."
    show monika at thide zorder 4
    hide monika
    window hide
    pause(1.0)
    show sayori 2zc at f11 zorder 4
    s "Ты хочешь побыть со мной? Ты меня сегодня поражаешь, [player]."
    s "Сначала вступил в мой клуб, а сейчас хочешь говорить со мной больше, чем обычно."
    s 2g "..."
    s 2h "Всё в порядке?"
    show sayori 2g at t11 zorder 4
    mc "Да, нет ничего же неправильного в том, чтобы побыть с тобой, верно?"
    show sayori 1l at f11 zorder 4
    s "...Конечно нет."
    s 1zc "Давай тогда сядем там."
    show sayori at thide zorder 4
    hide sayori
    "Она начинает замечать..."
    "Я знаю, что могу ей помочь, поэтому мне нужно говорить с ней чаще."
    "В то же время мне нельзя забывать об остальных... Это будет сложнее, чем я думал."
    "Если начнутся проблемы, мне придётся {w=1}{i}действовать быстро{/i}."
    scene bg club_day with wipeleft_scene
    stop music fadeout 1.0
    play music t2
    show sayori 5b at f11 zorder 4
    s "[player], Юри наверняка ждёт, когда ты с ней поговоришь, может, пойдёшь?"
    s 1x "О, и не беспокойся обо мне, я могу подождать."
    show sayori 1a at t11 zorder 4
    mc "Ну... раз ты так говоришь, я пойду к Юри."
    mc "Береги себя, [persistent.sayoriname]."
    show sayori 4r at f11 zorder 4
    s "Не сомневайся во мне!"
    show sayori at t11 zorder 4
    "У меня нехорошее предчувствие насчёт этого всего."
    "Но ещё слишком рано, сейчас она ничего не сделает."
    "Я уже должен идти к Юри, она достаточно ждала."
    scene bg club_day with wipeleft_scene
    show yuri 1f at f11 zorder 4
    y "Ох, ты здесь."
    show yuri at t11 zorder 4
    mc "Извини, что заставил ждать, я не специально."
    show yuri 2d at f11 zorder 4
    y "Нет, всё хорошо, я очень терпеливая."
    y 2b "Я понимаю, что ты можешь не жаждать разговаривать с незнакомцами."
    show yuri 2a at t11 zorder 4
    mc "Это совсем не так. Может, я и асоциальный, но я честно хочу поговорить с тобой."
    mc "Чем лучше я тебя узнаю, тем дольше мы пробудем."
    show yuri 4a at f11 zorder 4
    y "Да... ты прав."
    show yuri at thide zorder 4
    hide yuri
    "Мне нужно также сконцентрироваться на [persistent.sayoriname]..."
    "Мое внимание усиливается, моя радужка становится ярко-оранжевой и в результате начинает очень слабо светиться."
    show yuri 2e at f11 zorder 4
    y "..."
    y 2f "[player], у тебя такой красивый цвет глаз, я прежде никогда таких не видела."
    show yuri at t11 zorder 4
    mc "Цвет глаз? Он такой же, как у Моники, о чём ты?"
    show yuri 1f at f11 zorder 4
    y "Нет, не такой же. Они оранжевые."
    y "Какой необычный цвет."
    show yuri 1e at t11 zorder 4
    "Оранжевый?"
    "..."
    "Ах! Как я мог не заметить?!"
    mc "Извини, я на минутку..."
    "Я закрыл глаза."
    "Мне остаётся надеяться, что смена цвета глаз в этом мире – нормальное явление."
    "Отличное начало..."
    mc "Хорошо, теперь они нормальные."
    show yuri 3n at f11 zorder 4
    y "Т-ты можешь менять цвет глаз?!"
    show yuri at t11 zorder 4
    mc "Не совсем, это происходит само собой иногда."
    "Это для твоего же блага, Юри, я пока не могу тебе сказать правду."
    show yuri 1d at f11 zorder 4
    y "Не могу поверить, твои глаза могут менять цвет!"
    y 1b "Это такая редкость, я раньше про такое не слышала."
    y 1f "Если честно, я была убеждена, что это неправда."
    show yuri 1e at t11 zorder 4
    mc "Рад, что научил тебя чему-то новому."
    show yuri 3b at f11 zorder 4
    y "Твои глаза должны быть особенными, ты часто читаешь?"
    show yuri at t11 zorder 4
    mc "Мне тяжело даже прикоснуться к книге, так что, нет."
    mc "Если честно, я за всю жизнь не дочитал ни единой книги."
    show yuri 2v at f11 zorder 4
    y "Ох... Понятно, мы можем не читать, если не хочешь."
    show yuri at t11 zorder 4
    mc "Нет, я искренне хочу почитать с тобой."
    mc "Одна проблема: я явно читаю гораздо медленнее, чем ты."
    show yuri 3d at f11 zorder 4
    y "Ничего страшного, я подожду, только сообщи, когда можно будет перелистнуть страницу."
    y 1b "Эта книга по жанру фэнтези, тебя устроит?"
    show yuri at t11 zorder 4
    mc "Фэнтези – это мой любимый жанр, так что, да, конечно."
    show yuri 2f at t11 zorder 4
    "Её глаза загорелись в тот момент, когда я это сказал. Она, должно быть, очень рада это слышать."
    "Это логично, её любимые темы – хоррор и фэнтези, насколько я помню."
    show yuri 2d at f11 zorder 4
    y "Великолепно! Давай начнём прямо сейчас."
    show yuri at thide zorder 4
    hide yuri
    "Я заметил, что Моника что-то подготавливает."
    "Ей даже не нравится то, что я всё знаю, но она может поверить в то, что всё это был сон."
    "Если только та пустая пустота, в которой мы разговаривали ранее, не является особым местом, куда она может попасть, когда захочет."
    "В любом случае, в любой момент следует ожидать новых дел, и какими бы они ни были, я должен быть настороже."
    scene bg club_day with wipeleft_scene
    show monika 3b at f11 zorder 4
    m "Итак, друзья!"
    m "Теперь, когда у нас есть новый участник, я должна рассказать ему всё, что нужно."
    m 1k "Пожалуйста, подождите нас минутку... Спасибо!"
    show monika at thide zorder 4
    hide monika
    "Хорошего разговора не будет, но будь что будет, это цена моего поступка, всё-таки."
    show yuri 3b at f11 zorder 4
    y "Я могу подождать, поторопись, это важно для тебя."
    y "Для тебя будет важная информация о том, что мы тут делаем."
    show yuri 3a at t11 zorder 4
    mc "Понял, я скоро буду."
    show yuri at thide zorder 4
    hide yuri
    "Что она хочет мне сказать?.."
    "Не то, чтобы мне нужно было так много знать об этом клубе, на самом деле всё довольно просто для понимания."
    "Я чувствую, что она хочет поговорить о нашем предыдущем разговоре."
    window hide
    pause(1.0)
    scene bg corridor with wipeleft_scene
    stop music fadeout 1.0
    play music m1
    show monika 1h at t11 zorder 4
    m "..."
    show monika 1i at f11 zorder 4
    m "Я хочу у тебя кое-что спросить."
    m "Как ты сюда попал из реального мира?"
    m "И как много ты обо мне знаешь?"
    show monika at t11 zorder 4
    "Так предсказуемо."
    mc "Хорошо, если ты действительно хочешь знать, то..."
    mc "У меня нет причин не рассказывать тебе, однако есть одна вещь, которую я хочу прояснить."
    mc "Тебе лучше быть осторожной с твоим выбором и твоими желаниями."
    show monika 1s at f11 zorder 4
    m "О... О чём ты?"
    show monika at t11 zorder 4
    mc "Подумай ещё раз, прежде чем сделать что-то, это моё предупреждение."
    mc "Это сейчас важно для тебя, я расскажу тебе всё, что хочешь знать, но только после того, как ты будешь готова понять."
    show monika 1o at f11 zorder 4
    m "{w=0.5}.{w=0.5}.{w=0.5}."
    show monika 1v at t11 zorder 4
    pause(1.5)
    show monika 3v at t11 zorder 4
    call updateconsole("$ß*>÷->*¤<") from _call_updateconsole_15
    call hideconsole from _call_hideconsole_2
    show screen tear(25, 0.05, 0.05, -20, 80)
    play sound "sfx/glitch2.ogg"
    window hide
    pause(0.6)
    hide screen tear
    $ consolehistory = []
    show monika 1s at t11 zorder 4
    pause(3.0)
    show monika 3s at t11 zorder 4
    call updateconsole("¤$ß*>÷¤->÷*¤<") from _call_updateconsole_16
    call hideconsole from _call_hideconsole_3
    show screen tear(25, 0.05, 0.05, -20, 80)
    play sound "sfx/glitch2.ogg"
    window hide
    pause(0.6)
    hide screen tear
    $ consolehistory = []
    show monika 1s at t11 zorder 4
    pause(2.0)
    mc "Ты правда думала, что всё будет легко?"
    mc "Ты больше не можешь этим пользоваться."
    show monika 1s at f11 zorder 1
    m "Ч-что ты наделал?"
    m "Почему я не мо...{nw}"
    show monika at t11 zorder 4
    mc "Не можешь использовать консоль?"
    mc "Я не позволяю тебе это делать."
    mc "Пока я здесь, все твои попытки тщетны."
    show monika 1s at t11 zorder 4
    window hide
    pause(2.0)
    show monika 2p at f11 zorder 4
    m "Я просто хотела..."
    m 2o "..."
    show monika at t11 zorder 4
    mc "Я возвращаюсь к Юри, береги себя."
    scene bg club_day with wipeleft_scene
    stop music fadeout 1.0
    window hide
    pause (1.0)
    play music t2
    show yuri 1b at f11 zorder 4
    y "Ты вернулся! Как всё прошло?"
    show yuri 1a at t11 zorder 4
    mc "Прошло хорошо, ничего нового, продолжим?"
    show yuri 2d at f11 zorder 4
    y "Да!"
    show yuri at thide zorder 4
    hide yuri
    "Я слегка подзабыл о Нацуки, но как мне с ней заговорить?"
    "...Мне надо быстро придумать."
    scene bg black with dissolve_scene_full
    "Пятнадцать минут прошло."
    scene bg club_day with dissolve_scene_full
    show yuri 1f at f11 zorder 4
    y "Хорошо, закончим здесь? Уже пора идти домой."
    y "Я не хочу тебя здесь задерживать."
    show yuri 1e at t11 zorder 4
    mc "Без проблем, мы продолжим в следующий раз."
    mc "Мне ещё надо поговорить с Нацуки, чтобы она тоже узнала меня."
    show yuri 1d at f11 zorder 4
    y "Я не против!"
    y 3b "До завтра, [player]."
    show yuri at thide zorder 4
    hide yuri
    "И как только она в конце могла дойти до тех ужасных вещей?"
    "Она такая приятная и вежливая, так тяжело вообразить её в другом амплуа, когда я здесь и сейчас." ###
    "Но я видел это, и не могу закрывать на это глаза."
    "Я буду сопротивляться этой судьбе, но перед этим мне нужно вернуться к [persistent.sayoriname]."
    scene bg corridor with dissolve_scene_full
    "[persistent.sayoriname] покинула кабинет пораньше, но я её ещё вижу."
    mc "[persistent.sayoriname]!"
    "Услышав меня, она обернулась."
    show sayori 4b at f11 zorder 4
    s "А?"
    s 5b "Оу, извини, я тебе обогнала."
    s 5a "Я хотела тебя подождать во дворе."
    show sayori at t11 zorder 4
    "Странно, она же ведь всегда ходила со своим другом?"
    "Возможно, это из-за моего здесь нахождения, теперь она может ещё больше отдалиться от меня."
    "К счастью, я этого не позволю, извини, [persistent.sayoriname]..."
    mc "Не страшно, но не делай так больше."
    mc "Я уже почти подумал о том, что ты забыла обо мне."
    show sayori 2h at f11 zorder 4
    s "Ох, извини, [player]."
    s 1zc "Я больше так не сделаю, обещаю."
    s 1c "Но я хотела тебе кое-что рассказать интересное."
    s "Моника обычно раздаёт какие-то клубные задания, но сегодня она этого не сделала."
    s 2h "Я переживаю, что с ней что-то случилось..."
    show sayori at t11 zorder 4
    "{i}Эх.{/i}"
    "Это наверняка из-за меня, она отвела других на задний план."
    "Но чего бояться, у неё же всё равно нет выбора."
    mc "Я едва с ней поговорил, так что не могу сказать, в порядке она или нет."
    show sayori 2g at f11 zorder 4
    s "Окей... Я и не ожидала, что ты знаешь."
    s 1x "Забудь, пойдём уже."
    show sayori at thide zorder 4
    hide sayori
    scene bg residential_day with wipeleft_scene
    stop music fadeout 1.0
    window hide
    pause(1.0)
    play music t9
    show sayori 1x at f11 zorder 4
    s "Итак... Как тебе первый день в клубе?"
    show sayori 1a at t11 zorder 4
    mc "Мне очень понравилось. Наверное, потому, что в маленьких клубах более комфортно."
    mc "Мы с Юри читали, мне кажется, она хорошая."
    show sayori 4r at f11 zorder 4
    s "Я рада это слышать!"
    s 2zc "Ты наконец-то заводишь новых друзей, [player]!"
    s 1zc "Завтра тебе нужно поговорить с ними больше, я уверена, они захотят с тобой дружить."
    show sayori 1d at t11 zorder 4
    "Это явная попытка отстранить меня от неё."
    "Я не дам этому случиться, [persistent.sayoriname]."
    mc "Это, конечно, приятно, когда есть, с кем поговорить."
    mc "Но я ещё хочу проводить время с тобой."
    show sayori 2g at t11 zorder 4
    window hide
    pause(1.0)
    show sayori 2h at f11 zorder 4
    s "Но... Юри же хочет быть с тобой!"
    s 2zc "Пожалуйста, не трать на меня время, мне хорошо быть одной."
    show sayori 2d at t11 zorder 4
    "А мне – нет."
    mc "Мне важно разговаривать и с тобой, понимаешь."
    show sayori 1g at t11 zorder 4
    mc "Ты познакомила меня с ними, без тебя я бы их даже не узнал."
    window hide
    pause(2.3)
    show sayori 1k at f11 zorder 4
    s "Ладно..."
    s 1h "Пожалуйста, пообещай, что не забудешь о них."
    show sayori 1g at t11 zorder 4
    "Я почти никогда не даю обещаний, но я и не отказываюсь от своих слов."
    mc "Я обещаю."
    show sayori 1d at t11 zorder 4
    window hide
    pause(1.0)
    show sayori 4r at f11 zorder 4
    s "Хорошо, до завтра, [player]!"
    show sayori at thide zorder 4
    hide sayori
    "..."
    "Я просто хочу видеть её счастливой..."
    "Почему она должна быть обременена этим, почему именно она?!"
    "..."
    "Я буду поступать по-другому, и я спасу тебя, [persistent.sayoriname]."
    "Клянусь..."
    stop music fadeout 2.0
    scene bg bedroom with wipeleft_scene
    window hide
    pause(1.0)
    "Было бы хорошо вовремя разбудить [persistent.sayoriname]..."
    "Она же наверняка проспит..."
    "Утро вечера мудренее, мне тоже надо выспаться."
    "Кто знает, к чему мне стоит быть готовым."
    window hide
    pause(1.0)
    scene bg black with dissolve_scene_full
    pause(0.5)
    play music m1
    show monika 1h at t11 zorder 4
    pause(0.7)
    "..."
    "Моника?"
    show monika 1i at f11 zorder 4
    m "Почему ты не скажешь мне?"
    m "Ты просто шутишь надо мной??"
    show monika at t11 zorder 4
    mc "Зачем мне это делать, в чём смысл?"
    mc "Ты уже видела мои воспоминания, и тебе их должно хватить."
    mc "Я хочу выспаться, чтобы разбудить [persistent.sayoriname] пораньше, давай поговорим в школе."
    show monika 5c at f11 zorder 4
    m "Хватит о ней думать!{w=0.5} Если ты правда из реального мира, то ты должен знать, что она...{nw}"
    show monika at t11 zorder 4
    mc "Даже не смей говорить об этом."
    mc "Единственный, кто здесь ведёт себя, как не по-человечески, так это ты."
    show monika 1x at t11 zorder 4
    window hide
    pause(2.0)
    mc "Я не хочу этого, Моника."
    mc "Ты можешь думать, что [persistent.sayoriname] безнадёжна, но я так думать не собираюсь."
    mc "Каждый день она правда превозмогает, и если ты даже не можешь признать, что..."
    show monika 2o at t11 zorder 4
    window hide
    pause(2.0)
    show monika 1i at f11 zorder 4
    m "Ты ей не поможешь, никто не поможет."
    show monika 1h at t11 zorder 4
    mc "Ты ошибаешься, Моника."
    mc "Ты стоишь на пути к моим целям, а ты даже половину их не видела."
    mc "Я пришёл сюда, чтобы делать правильные поступки и спасти всех, так что, убирайся из моей головы!"
    show monika 1s at t11 zorder 4
    mc "{b}Убирайся{w=0.25} из{w=0.25} моей{w=0.25} головы.{/b}"
    stop music fadeout 0.1
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause(0.25)
    show monika at thide zorder 4
    hide monika
    hide screen tear
    pause(1.0)
    scene bg bedroom with dissolve_scene_full
    pause(2.0)
    "..."
    "Мне надо идти будить [persistent.sayoriname]."
    scene bg house with wipeleft_scene
    window hide
    pause(1.0)
    "Я тут, [persistent.sayoriname]..."
    menu: #Options
        "Громко позвать её":
            $ value = 1
        "Войти в дом":
            $ value = 2
        "Уйти":
            $ value = 3
    if value == 1:
        mc "[persistent.sayoriname]!"
        "Она услышала меня и вышла на улицу."
        play music t2
        show sayori 2bb at f11 zorder 4
        s "Ох, привет, [player], что ты здесь делаешь?"
        show sayori at t11 zorder 4
        mc "Я хотел убедиться, что ты не проспишь."
        show sayori 1bl at f11 zorder 4
        s "Тебе правда не стоило, но спасибо."
        show sayori at t11 zorder 4
        mc "Я подожду, пока ты оденешься, не торопись."
        show sayori 1bx at f11 zorder 4
        s "Хорошо!"
        show sayori at thide zorder 4
        hide sayori
        window hide
        pause(0.5)
        "Должно сработать."
        jump phase2
    if value == 2:
        "Я вошёл в дом."
        scene bg house_corridor with wipeleft_scene
        window hide
        pause(1.0)
        "Она наверняка в своей комнате."
        "Я постучался в дверь."
        mc "[persistent.sayoriname]? Ты не спишь?"
        "Я расслышал тихий шорох из её комнаты."
        "Она открыла дверь."
        show sayori 2bb at f11 zorder 4
        play music t2
        s "[player]? Что ты здесь делаешь?"
        show sayori at t11 zorder 4
        mc "Я тут, чтобы убедиться, что ты не проспишь."
        mc "Последнее, что я хочу, это то, что ты не придёшь на встречу клуба."
        show sayori 1bl at f11 zorder 4
        s "Оу-у... Ты же знаешь, не надо обо мне беспокоиться."
        s 1bx "Я пойду оденусь."
        show sayori 1ba at t11 zorder 4
        mc "Окей, я тебя подожду здесь."
        show sayori at thide zorder 4
        hide sayori
        "Немного странно, что я вот так вошёл в её дом."
        "Но она не злится, и это гарантирует, что она придёт на встречу."
        "Это всё важно для меня."
        show sayori 2r at f11 zorder 4
        s "Я готова!"
        jump phase2
    if value == 3:
        "..."
        "{w=0.6}Ты {w=0.6}себя {w=0.6}не {w=0.6}контролируешь{w=0.6}."
        scene bg end-glitch #Basic use for showing a moving glitch screen with sound
        window hide
        pause(0.01) #Needs to be there to show the glitch screen with screen tear
        show screen tear(25, 0.1, 0.1, 0, 60)
        play sound "sfx/glitch2.ogg"
        pause(0.5)
        scene bg house #Original BG that was there before the effect
        hide screen tear #Ends here!
        "Я вошёл в дом."
        scene bg house_corridor with wipeleft_scene
        window hide
        pause(1.0)
        "Она наверняка в своей комнате."
        "Я постучался в дверь."
        mc "[persistent.sayoriname]? Ты не спишь?"
        "Я расслышал тихий шорох из её комнаты."
        "Она открыла дверь."
        show sayori 2bb at f11 zorder 4
        play music t2
        s "[player]? Что ты здесь делаешь?"
        show sayori at t11 zorder 4
        mc "Я тут, чтобы убедиться, что ты не проспишь."
        mc "Последнее, что я хочу, это то, что ты не придёшь на встречу клуба."
        show sayori 1bl at f11 zorder 4
        s "Оу-у... Ты же знаешь, не надо обо мне беспокоиться."
        s 1bx "Я пойду оденусь."
        show sayori 1ba at t11 zorder 4
        mc "Окей, я тебя подожду здесь."
        show sayori at thide zorder 4
        hide sayori
        "Немного странно, что я вот так вошёл в её дом."
        "Но она не злится, и это гарантирует, что она придёт на встречу."
        "Это всё важно для меня."
        show sayori 2r at f11 zorder 4
        s "Я готова!"
        jump phase2

label phase2:
    scene bg corridor with wipeleft_scene
    pause(0.5)
    show sayori 1y at f11 zorder 4
    s "[player], может, уйдёшь без меня? Я приду попозже."
    show sayori at t11 zorder 4
    "Она снова пытается..."
    "Прости, что давлю на тебя, [persistent.sayoriname]..."
    "Но я это делаю ради тебя, ты это скоро осознаешь."
    mc "В чём проблема, [persistent.sayoriname]?"
    show sayori 2d at f11 zorder 4
    s "Проблем нет, дурачок."
    s "Я просто не хочу мешать тебе проводить время с другими."
    show sayori at t11 zorder 4
    mc "О чём ты говоришь? Ты мне не мешаешь."
    mc "К тому же, я говорил тебе, что хочу быть с тобой, так ведь?"
    show sayori 1k at t11 zorder 4
    stop music fadeout 2.5
    window hide
    pause(3.0)
    show sayori at f11 zorder 4
    play music t9
    s 1h "Почему ты хочешь тратить время на меня?"
    s "Я этого не заслуживаю! Я...{nw}"
    show sayori at t11 zorder 4
    mc "Хватит."
    show sayori 1g at t11 zorder 4
    window hide
    pause(2.5)
    mc "[persistent.sayoriname], ты важна для меня."
    mc "Прошу... пойми это, я хочу только лучшего для тебя."
    show sayori 3g at t11 zorder 4
    "Я нежно беру её за руку."
    mc "Ты важна для меня так, как нельзя описать словами."
    show sayori 3v at t11 zorder 4
    window hide
    pause(1.2)
    show sayori at f11 zorder 4
    s "Я просто... не хочу, чтобы ты беспокоился обо мне."
    show sayori 3u at t11 zorder 4
    mc "Всё хорошо. Если у тебя будут проблемы, я помогу с ними."
    mc "Я здесь ради тебя, и я не хочу, чтобы тебя что-то беспокоило."
    show sayori 1v at f11 zorder 4
    s "Ты это честно?"
    show sayori at t11 zorder 4
    mc "Конечно, честно."
    show sayori 1t at t11 zorder 4
    window hide
    pause(1.5)
    show sayori 1zd at f11 zorder 4
    s "Спасибо, [player]..."
    show sayori 1t at t11 zorder 4
    mc "Без проблем, [persistent.sayoriname]."
    mc "Нам пора идти, нас заждались."
    show sayori 1zc at f11 zorder 4
    s "Да!"
    scene bg club_day with wipeleft_scene
    stop music fadeout 3.0
    window hide
    pause(4.0)
    "Я чувствую себя... странно, что происходит?"
    show sayori 2b at f11 zorder 4
    s "[player]? Ты в порядке?"
    show sayori at t11 zorder 4
    play music hb
    show vignette: #Dark effect around the sides
        alpha 1.0
    show layer master at heartbeat #Heartbeat music
    window hide
    pause(2.0)
    mc "С... [persistent.sayoriname]..."
    "Почему я не могу чётко говорить?"
    "Я никогда прежде такого не чувствовал..."
    "Я..."
    show sayori 4w at f11 zorder 4
    s "[player]!!"
    scene bg black with dissolve_scene_full
    stop music fadeout 2.0
    window hide
    pause(1.0)
    show layer master #End of heartbeat music
    hide vignette #End of the dark effect
    "..."
    "В чём смысл?!"
    scene bg end-glitch2
    window hide
    pause(0.01)
    show screen tear(27, 0.1, 0.1, 0, 65)
    play sound "sfx/glitch1.ogg"
    window hide
    pause(1.0)
    scene bg black
    hide screen tear
    mc "Хватит уже, Моника."
    mc "Эти фокусы на меня не действуют, выходи и поговори со мной лицом к лицу!"
    show yuri 3y4 at t11 zorder 4
    "..."
    "Что?"
    "Почему я вижу Юри? Она просто не может..."
    mc "Юри? Это ты?"
    show yuri 3y3 at f11 zorder 4
    play music hb
    show layer master at heartbeat
    y "Конечно же я, ты разве не узнаёшь меня, [player]?"
    y "Мне очень понравилось, как мы вчера провели время!"
    y "Нам стоит это повторить!"
    y "Не бросай меня, мы будем вместе навсегда."
    show yuri at t11 zorder 4
    mc "Хватит!"
    show yuri 3y7 at t11 zorder 4
    mc "Эта не та Юри, которую я знаю, прекрати этот бред!"
    show layer master
    stop music
    mc "{b}Я не дам тебе контролировать мой разум.{/b}"
    scene bg club_day with dissolve_scene_full
    pause(2.0)
    "Я очнулся рядом с [persistent.sayoriname]."
    play music t9
    show sayori 4w at f11 zorder 4
    s "[player]! Пожалуйста, проснись!"
    show sayori 4v at t11 zorder 4
    "Что за чертовщина произошла?"
    "Я полностью невосприимчив ко всем манипуляциям и контролю."
    "Это было что-то другое..."
    mc "Прости, [persistent.sayoriname], я отключился."
    mc "Сейчас я в порядке."
    show sayori 1t at t11 zorder 4
    window hide
    pause(1.2)
    show sayori 1zd at f11 zorder 4
    s "Ты меня перепугал, это было так неожиданно."
    show natsuki 2m at f22 zorder 3
    show sayori 1t at t21 zorder 4
    n "Эй, [player], можешь уходить, если себя плохо чувствуешь."
    show natsuki 2n at t22 zorder 3
    mc "Нет, я в норме, я хочу быть здесь со всеми вами."
    show sayori 1d at t31 zorder 4
    show natsuki 2j at t32 zorder 3
    show yuri 2f at f33 zorder 2
    y "Хорошо, но не издевайся над собой, идёт?"
    show yuri 2e at t33 zorder 2
    mc "Не беспокойся, всё будет хорошо."
    mc "Кстати, а где Моника?"
    show natsuki 5w at f32 zorder 3
    stop music
    play music t2
    n "Эм... Она опять опаздывает, так безответственно."
    n 4l "Пока её нет, я могу приготовить для всех кексики."
    show natsuki 4j at t32 zorder 3
    show sayori 4r at h31 zorder 4
    s "Ура! Нацуки печёт лучшие кексики!"
    show sayori 4q at t31 zorder 4
    mc "Я хочу их попробовать."
    show sayori 1a at t31 zorder 4
    show natsuki 3z at f32 zorder 3
    n "Ладно, я скоро буду тут!"
    show natsuki at thide zorder 3
    hide natsuki
    show sayori 1a at t21 zorder 4
    show yuri 1b at f22 zorder 3
    y "[player], мы можем продолжить со страницы, на которой остановились вчера."
    show yuri 1a at t22 zorder 3
    mc "Конечно, но я сначала немного поболтаю с [persistent.sayoriname], окей?"
    show sayori 1b at t21 zorder 4
    show yuri 1d at f22 zorder 3
    y "Без проблем, хорошо проведите время!"
    show yuri at thide zorder 3
    hide yuri
    show sayori 2zc at f11 zorder 4
    s "Ты правда хочешь дружить со всеми, не так ли?"
    show sayori 2d at t11 zorder 4
    stop music fadeout 1.0
    window hide
    pause(1.0)
    play music t9
    mc "Да, от своих слов я не отказываюсь."
    mc "Всё-таки, у тебя всё хорошо, [persistent.sayoriname]?"
    show sayori 1y at f11 zorder 4
    s "Да, с тобой приятно, [player]."
    s 2zd "Когда ты рядом со мной, я чувствую себя... счастливой."
    show sayori 2t at t11 zorder 4
    "Я чувствую такое облегчение, слыша это."
    "Это всё, о чём я мог просить, но действительно ли она счастлива?"
    "Она не захочет говорить об этом сейчас, но, возможно, я смогу уговорить её сделать это позже."
    "..."
    "Я знаю, что делать."
    scene bg black with dissolve_scene_full
    window hide
    pause(0.1)
    "Я крепко обнимаю [persistent.sayoriname]."
    mc "[persistent.sayoriname]... ты же знаешь, что можешь быть открытой со мной?"
    s "[player]..."
    "Она обнимает меня в ответ, её пальцы вцепляются в мою спину."
    s "Спасибо... что дал клубу шанс, ты делаешь мою жизнь намного лучше."
    s "Я не знаю, как выразить свою благодарность."
    "Не может быть..."
    "Ещё так рано, а она делает подобные вещи?"
    "Это может означать лишь то, что сейчас я должен быть особенно осторожен."
    mc "Я всегда буду рядом с тобой, не забывай."
    mc "Ты можешь доверять мне насчёт этого."
    s "Я... доверяю тебе, [player]."
    window hide
    pause(2.0)
    "Мы потратили время на светские разговоры."
    "А Моника всё ещё не вернулась..."
    "Сейчас я уверен, что она сделала бы это и без моего влияния, но почему это произошло раньше?"
    "Разве она не должна быть сейчас на занятиях на пианино? А если да... Значит, она хотела сделать что-то ещё."
    scene bg club_day with dissolve_scene_full
    pause(1.0)
    show sayori 2c at f11 zorder 4
    s "[player], тебе пора переключиться на Юри, она заждалась."
    show sayori at t11 zorder 4
    mc "Уверена, что без меня тебе будет хорошо?"
    show sayori 2zc at f11 zorder 4
    s "Да, мы всё ещё будем неподалёку, в конце концов."
    s "Если мне будет одиноко, я могу подойти к тебе."
    show sayori 1d at t11 zorder 4
    mc "Естественно!"
    mc "Ну... Я пойду, береги себя, [persistent.sayoriname]."
    show sayori 4s at f11 zorder 4
    s "И ты!"
    show sayori at thide zorder 4
    hide sayori
    "Я ощущаю очень тревожное чувство."
    "Как будто она... хочет положить этому всему конец уже завтра..."
    "Это совсем скоро, так почему бы мне не..."
    show yuri 2d at f11 zorder 3
    stop music
    play music t8
    y "Ох, [player], ты уже здесь!"
    show yuri 2a at t11 zorder 3
    mc "Да, я же говорил, что приду."
    "Придётся оставить это на потом."
    "Ничего не произойдёт, пока я тут."
    show yuri at t21 zorder 3
    show natsuki 3d at f22 zorder 4
    n "Я тут! Быстро разбирайте, я хочу, чтобы вы это попробовали."
    show natsuki 3a at t22 zorder 3
    "Юри и я взяли по одному кексику."
    "Как только я его надкусил, я почувствовал яркий вкус."
    mc "Я никогда не ел такого вкусного кекса, ты хороша в готовке, не сомневайся."
    show yuri 3d at f21 zorder 4
    y "Согласна!"
    show natsuki 5y at f22 zorder 4
    show yuri 1a at t21 zorder 3
    n "Я же говорила, я не делаю ничего хуже идеала!"
    n 2d "Ладно, я ещё предложу [persistent.sayoriname]."
    n "Если захотите ещё, я оставлю их на столе, просто берите."
    show natsuki 2a at t22 zorder 3
    mc "Спасибо, Нацуки."
    show natsuki 1l at f22 zorder 4
    n "Без проблем, я пойду почитаю мангу, до скорого!"
    show natsuki at thide zorder 4
    hide natsuki
    show yuri 1h at f11 zorder 4
    y "[player], прежде, чем мы продолжим..."
    y 1f "Есть что-то конкретное, что ты хочешь знать об этом клубе?"
    show yuri 1e at t11 zorder 4
    menu:
        mc "Действительно, есть что-то, что я хочу спросить."
        "Какие отношения у тебя с [persistent.sayoriname]?":
            $ value = 4
        "Почему Моника вчера не дала никаких заданий?":
            $ value = 5
    if value == 5:
        mc "[persistent.sayoriname] сказала мне, что обычно Моника раздаёт разные задания."
        mc "Почему вчера она этого не сделала?"
        show yuri 1h at f11 zorder 4
        y "Я спрашивала себя о том же самом."
        y 1f "Может, у неё просто не было времени?"
        show yuri at t11 zorder 4
        "Я так и думал, это, скорее, из-за моего нахождения тут."
        "Но я пока не могу быть в этом особо уверен."
        mc "Возможно, это логично."
        menu:
            mc "Ещё... Хочу спросить напоследок кое-что."
            "Какие отношения у тебя с [persistent.sayoriname]?":
                $ value = 7
        if value == 7:
            mc "Я хочу знать, хорошо ли ты дружишь с [persistent.sayoriname]."
            show yuri 2d at f11 zorder 4
            y "Мы хорошо дружим."
            y 1b "[persistent.sayoriname] очень замечательный человек, она помогала мне всегда, когда мне это нужно было больше всего."
            show yuri 1a at t11 zorder 4
            mc "Я рад, что у вас нет проблем друг с другом."
            "Это облегчает мне задачу."
            mc "Слушай... ты когда-нибудь замечала в ней что-то странное?"
            show yuri 2f at f11 zorder 4
            y "Странное?"
            y 2h "Хм-м-м... Не могу сказать, не припоминаю ничего подобного."
            y 1e "А что-то случилось?"
            show yuri at t11 zorder 4
            mc "Не-а, просто спрашиваю..."
            jump phase3
    if value == 4:
        mc "Я хочу знать, хорошо ли ты дружишь с [persistent.sayoriname]."
        show yuri 2d at f11 zorder 4
        y "Мы хорошо дружим."
        y 1b "[persistent.sayoriname] очень замечательный человек, она помогала мне всегда, когда мне это нужно было больше всего."
        show yuri 1a at t11 zorder 4
        mc "Я рад, что у вас нет проблем друг с другом."
        "Это облегчает мне задачу."
        mc "Слушай... ты когда-нибудь замечала в ней что-то странное?"
        show yuri 2f at f11 zorder 4
        y "Странное?"
        y 2h "Хм-м-м... Не могу сказать, не припоминаю ничего подобного."
        y 1e "А что-то случилось?"
        show yuri at t11 zorder 4
        mc "Не-а, просто спрашиваю..."
        menu:
            mc "Ещё... Хочу спросить напоследок кое-что."
            "Почему Моника вчера не дала никаких заданий?":
                $ value = 6
        if value == 6:
            mc "[persistent.sayoriname] сказала мне, что обычно Моника раздаёт разные задания."
            mc "Почему вчера она этого не сделала?"
            show yuri 1h at f11 zorder 4
            y "Я спрашивала себя о том же самом."
            y 1f "Может, у неё просто не было времени?"
            show yuri at t11 zorder 4
            "Я так и думал, это, скорее, из-за моего нахождения тут."
            "Но я пока не могу быть в этом особо уверен."
            mc "Возможно, это логично."
            jump phase3
label phase3:
    mc "Что ж... Я выяснил всё, что хотел, спасибо."
    show yuri 3d at f11 zorder 4
    y "Не за что, [player]!"
    show yuri at thide zorder 4
    hide yuri
    "Мы вместе продолжили чтение."
    "Я услышал, как кто-то зашёл..."
    show monika 2n at f11 zorder 4
    m "Всем привет, простите, что я так опоздала сегодня."
    show monika 2a at t21 zorder 3
    show natsuki 5w at f22 zorder 4
    n "Ты очень сильно опоздала."
    n 3h "У тебя были какие-то дела?"
    show natsuki at t22 zorder 3
    show monika 2b at f21 zorder 4
    m "Ничего важного, правда, просто много мелких проблем."
    show monika at t21 zorder 3
    show natsuki 1c at f22 zorder 4
    n "Ну ладно, но в следующий раз давай без этого."
    show natsuki 1g at t22 zorder 3
    show monika 2l at f21 zorder 4
    m "Не переживай, Нацуки."
    m 2y "Но спасибо за заботу."
    show natsuki at thide zorder 3
    hide natsuki
    show monika 2b at f11 zorder 4
    m "Я пойду за свой стол, позовите, если буду нужна."
    show monika at thide zorder 4
    hide monika
    "Мелкие проблемы, говоришь?"
    "Или она снова пытается повлиять на них..."
    show natsuki 1c at f11 zorder 4
    n "[player], извини, что отвлекаю, но можно..."
    show natsuki 1s at f11 zorder 4
    window hide
    pause(1.0)
    show natsuki 1q at f11 zorder 4
    n "Можно потусоваться с тобой, когда мы уйдём?"
    show natsuki 1s at t11 zorder 3
    mc "Да, почему нет."
    show natsuki 1k at t11 zorder 3
    "Кажется, она весьма удивлена моим ответом."
    "Они сейчас все хотят быть со мной?"
    show natsuki 2l at f11 zorder 4
    n "Круто! Я буду ждать во дворе."
    show natsuki at thide zorder 3
    hide natsuki
    window hide
    pause(1.0)
    show yuri 1f at f11 zorder 4
    y "Ты хочешь проводить с нами время вне клуба?"
    y 4a "Нет, в этом нет ничего плохого, просто спрашиваю."
    show yuri at t11 zorder 4
    "В другой ситуации я бы этого не сделал, но, раз я сейчас здесь..."
    "Совсем не обязательно иметь много свободного времени."
    mc "Важно узнавать всех вас получше."
    mc "Кроме того... Мне нравится быть здесь, я рад, что вступил в Литературный клуб."
    show yuri 3d at f11 zorder 4
    y "Я тоже рада!"
    y 1f "Кстати... Давай оставим остальное на завтра."
    show yuri at t11 zorder 4
    mc "Давай, завтра как раз дочитаем."
    show yuri 2b at f11 zorder 4
    y "Ты бы хотел почитать какую-нибудь книгу со мной?"
    show yuri 2a at t11 zorder 4
    "Есть несколько в том месте, откуда я пришёл, но не взял их с собой, как жаль."
    mc "Полагаю, если я найду что-нибудь у себя, я скажу."
    show yuri 1d at f11 zorder 4
    y "Хорошо!"
    show yuri at thide zorder 4
    hide yuri
    "Спустя пять минут настало время уходить."   ####половина
    show monika 4b at f11 zorder 4
    m "Итак, друзья!"
    m 2l "Извините, что вчера не дала вам заданий."
    m 3b "В качестве компенсации я сейчас раздам что-нибудь интересное."
    m 5a "Каждый должен написать стихотворение на завтра, выбирайте тему на ваше усмотрение!"
    m 1b "Я с нетерпением жду ваших работ, хорошего вечера."
    m "До завтра!"
    show monika at thide zorder 3
    hide monika
    "ЭТо было ожидаемо, к счастью, я подготовился."
    show yuri 1f at f11 zorder 4
    y "Стихотворение? Это что-то новенькое."
    y 2b "В любом случае, спасибо, что был со мной, [player]."
    y 2d "Увидимся завтра!"
    show yuri 2c at t11 zorder 4
    mc "Ага, до завтра!"
    show yuri at thide zorder 4
    hide yuri
    "Я пока не вижу никаких знаков, может, они появятся после инцидента с [persistent.sayoriname]..."
    "Кажется, у всех всё хорошо... Какое облегчение."
    "[persistent.sayoriname] ждёт меня за дверью, не буду заставлять её ждать."
    scene bg corridor with wipeleft_scene
    window hide
    pause(1.0)
    show sayori 2x at f11 zorder 4
    s "[player], Моника нам сказала написать на завтра стихотворение!"
    s 1r "Я думаю, она просто была занята раньше."
    show sayori 1a at t11 zorder 4
    mc "Я удивлён, о чём будешь писать?"
    show sayori 4r at f11 zorder 4
    s "Секрет!"
    s 1x "Не волнуйся, тебе определённо понравится."
    show sayori 1a at t11 zorder 4
    mc "Не сомневаюсь, [persistent.sayoriname]."
    show sayori at thide zorder 4
    hide sayori
    "Вместе мы вышли на улицу."
    show bg residential_day with dissolve_scene_full
    window hide
    pause(1.2)
    play music t9
    show sayori 2l at f11 zorder 4
    s "Сегодня был тяжеловатый день."
    s 2h "Ты в порядке?"
    show sayori 2g at t11 zorder 4
    mc "В порядке, говорю же, это просто была маленькая отключка."
    show sayori 1d at t11 zorder 4
    "На самом деле... Я не могу забыть о том, что я там увидел, странно."
    "Почему я видел Юри, а не Монику? Это всё намеренно?"
    show sayori 2zd at f11 zorder 4
    s "Я рада знать об этом."
    s 1v "Я не могу видеть тебя таким."
    show sayori at t11 zorder 4
    mc "Не переживай, [persistent.sayoriname], я так просто не вырублюсь."
    show sayori 1t at t11 zorder 4
    window hide
    pause(1.0)
    show sayori 2zc at f11 zorder 4
    s "Хорошо, я тебе верю, [player]."
    show sayori 1x at f11 zorder 4
    s "До завтра!"
    show sayori at thide zorder 4
    hide sayori
    "Я направился к ждущей меня Нацуки, после того, как мы с [persistent.sayoriname] разошлись, а её я проведаю ещё раз."
    "Проснуться завтра рано очень важно, я должен это сделать это любой ценой."
    show natsuki 4l at f11 zorder 4
    stop music
    play music t2
    n "Явился, не запылился."
    n 5y "А я думала, ты забудешь обо мне."
    show natsuki 1a at t11 zorder 4
    mc "Почему я должен был забыть о тебе?"
    mc "Мы же договорились встретиться после школы."
    mc "В общем, чем хочешь заняться?"
    show natsuki 2t at f11 zorder 4
    n "Я знаю."
    n 4d "Давай на завтра напечём кексиков."
    show natsuki 5w at f11 zorder 4
    n "[persistent.sayoriname] съела почти их все, всё в одну харю!"
    show natsuki 5x at t11 zorder 4
    mc "Ха-ха... Типичная [persistent.sayoriname]."
    show natsuki 1j at t11 zorder 4
    mc "Но есть один нюанс... Я не умею печь."
    mc "Я никогда прежде ничего не готовил."
    show natsuki 2z at f11 zorder 4
    n "Без проблем, я тебе покажу."
    n 1d "Это не сложно, ты быстро разберёшься."
    show natsuki 1a at t11 zorder 4
    mc "Ага... Полагаю, будет лучше, если мы будем на моей кухне."
    mc "На всякий случай."
    show natsuki 3y at f11 zorder 4
    n "Я не против, альтернатив всё равно нет."
    show natsuki at t11 zorder 4
    scene bg kitchen with wipeleft_scene
    window hide
    pause(0.5)
    "Я всё ещё не знаю, как помочь Нацуки с её проблемой."
    "Она, наверное, не хочет, чтобы кто-то помогал ей."
    show natsuki 5y at f11 zorder 4
    n "Я покажу тебе, что такое профессиональная готовка."
    n 1l "Просто подавай ингредиенты, которые я покажу."
    show natsuki 1a at t11 zorder 4
    mc "Надеюсь, у меня есть всё необходимое."
    "Я не знаю, что лежит в моём холодильнике, но разве я буду говорить ей, что я из другого мира?"
    "Кто в такую ерунду поверит..."
    show natsuki 2c at f11 zorder 4
    n "Ну давай тогда посмотрим, что у тебя есть."
    show natsuki at thide zorder 4
    hide natsuki
    "Нацуки начинает обыскивать всю мою кухню, постепенно собирая всё, что ей нужно."
    show natsuki 1c at f11 zorder 4
    n "У тебя действительно есть все ингредиенты."
    show natsuki 1a at t11 zorder 4
    "Это весьма удивительно."
    mc "Итак... С чего начнём?"
    show natsuki 4y at f11 zorder 4
    n "Ты и правда бестолковый."
    n 4l "Давай, сейчас покажу."
    scene bg black with dissolve_scene_full
    window hide
    pause(0.1)
    "За время обучения нам удалось вместе успешно испечь несколько кексов."
    "Но в процессе я также почувствовал нечто знакомое, и у меня нехорошее предчувствие по этому поводу..."
    scene bg kitchen with dissolve_scene_full
    show natsuki 3k at f11 zorder 4
    n "Мы с тобой молодцы."
    n 3l "Полагаю, ты не так уж и плох в готовке."
    show natsuki 3a at t11 zorder 4
    mc "Всё благодаря тебе, я бы сам не знал, что делать со всеми ингредиентами."
    mc "Всё же было весело, надо будет ещё раз как-нибудь попробовать."
    show natsuki 4z at f11 zorder 4
    n "Естественно!"
    n 1m "Но мне уже надо идти, хотя я хотела бы ещё побыть."
    show natsuki 1n at t11 zorder 4
    mc "Да, но у нас ещё много дней впереди."
    "Пока я могу справляться со всей этой ситуацией, в которую я попал."
    "Но я делаю это ради них, это моя воля и мои амбиции."
    show natsuki 2s at t11 zorder 4
    window hide
    pause(1.0)
    show natsuki 2q at f11 zorder 4
    n "Я... не особо хочу возвращаться домой."
    show natsuki 2s at t11 zorder 4
    "Бедная Нацуки, я помогу, как только смогу, она заслуживает этого так же, как и другие."
    mc "Почему?"
    show natsuki 1p at f11 zorder 4
    n "Нет! То есть..."
    show natsuki 1r at t11 zorder 4
    window hide
    pause(1.3)
    show natsuki 5q at f11 zorder 4
    n "Неважно, просто забудь."
    n 1l "Увидимся завтра после уроков!"
    show natsuki at thide zorder 4
    hide natsuki
    "Я был прав... она не хочет, чтобы ей кто-то помогал, тем более, с её-то проблемой."
    "Интересно, как же я справлюсь..."
    stop music fadeout 2.5
    "{w=0.5}.{w=0.5}.{w=0.5}."
    "Это чувство, оно возвращается ко мне."
    "Мне нужно проверить [persistent.sayoriname] прямо сейчас!"
    scene bg house with wipeleft_scene
    window hide
    pause(1.0)
    "Прежде чем я успеваю сделать ещё шаг, я вижу, как она выходит из дома."
    show sayori 2bl at f11 zorder 4
    play music t10
    s "Ох, [player], я не ожидала увидеть тебя здесь."
    show sayori at t11 zorder 4
    mc "[persistent.sayoriname]... ты пришла, потому что хотела мне что-то рассказать, я прав?"
    show sayori 1bk at t11 zorder 4
    window hide
    pause(1.0)
    show sayori 1bh at f11 zorder 4
    s "Это что-то не очень важное, правда..."
    show sayori 1bg at t11 zorder 4
    mc "Я отказываюсь в это верить."
    mc "Расскажи, что тебя тревожит."
    mc "Помни, что я здесь, чтобы тебе помочь..."
    show sayori 2bu at t11 zorder 4
    window hide
    pause(1.0)
    show sayori 2bv at f11 zorder 4
    s "[player], я..."
    s "Так тяжело об этом говорить..."
    s 1bv "Я не хочу, чтобы ты испугался того, что я скажу."
    show sayori at t11 zorder 4
    mc "Я не испугаюсь."
    mc "Что бы там ни было, это должно быть важно, если это тебя тревожит!"
    show sayori 1bt at f11 zorder 4
    s "..."
    s 1bzd "[player], когда ты присоединился к моему клубу, я стала чувствовать себя лучше."
    s 2bzd "Ты завёл новых друзей, ты начал проводить со мной больше времени."
    s 1bv "И я должна быть рада за тебя."
    s "Но оно болит... очень сильно болит..."
    s 4bw "Почему оно болит?! Я не хочу это чувствовать!"
    show sayori 4bv at t11 zorder 4
    mc "Что именно ты не хочешь чувствовать?"
    show sayori 1bk at f11 zorder 4
    s "..."
    s 1bh "Правда в том, что..."
    s 1bv "У меня..."
    s "У меня депрессия, [player]."
    s "Это абсолютная правда, я не шучу."
    scene bg black with dissolve_scene_full
    window hide
    pause(0.1)
    "Без задней мысли, я резко подхожу к [persistent.sayoriname]."
    window hide
    pause(1.5)
    mc "Я бы никогда и не подумал."
    mc "Но, [persistent.sayoriname]... почему ты не рассказала мне раньше?"
    s "Прости, [player]."
    s "Я просто очень боялась... и я не хотела об этом разговаривать."
    s "Ты должен был веселиться со всеми, я бы просто это всё разрушила, если бы рассказала."
    mc "Нет, я был бы готов помочь тебе, и я уверен, что другие тоже помогли бы тебе, если бы могли."
    mc "Пожалуйста... больше не скрывай от меня ничего такого важного."
    s "Я... Я не буду, обещаю тебе."
    mc "Ты гораздо важнее для меня, чем ты думаешь, [persistent.sayoriname]."
    mc "Вот почему я не позволю тебе пройти через это самостоятельно."
    scene bg house with dissolve_scene_full
    window hide
    pause(0.5)
    show sayori 2bt at t11 zorder 4
    window hide
    pause(0.8)
    show sayori 2bzd at f11 zorder 4
    s "Я правда так много значу для тебя?"
    show sayori 2bt at t11 zorder 4
    mc "Правда."
    window hide
    pause(1.5)
    show sayori 1bzd at f11 zorder 4
    s "Я так рада, что в моей жизни есть такой человек."
    show sayori 2bk at f11 zorder 4
    s "Но уже темнеет, я пойду."
    s 1bh "Мне ещё надо написать стихотворение на завтра."
    show sayori 1bg at t11 zorder 4
    "Ах, конечно, я и забыл об этом."
    mc "Окей, мы увидимся завтра в любом случае."
    show sayori 1bl at f11 zorder 4
    s "Ага..."
    s 4bzc "Увидимся, [player]!"
    show sayori at thide zorder 4
    hide sayori
    "Когда она уходит, листок бумаги выпадает из её кармана."
    "...постой, что?"
    "Я подбираю его."
    stop music fadeout 2.0
    call showpoem(poem_s3, music=False) from _call_showpoem #Showing a poem without changing the music
    "{w=1}.{w=1}.{w=1}."
    "!!!"
    "Это... Это не может быть!"
    "Этот стих... это тот самый стих, который она написала, перед тем, как..."
    window hide
    pause(2.0)
    "Теперь я понимаю, мне надо вставать ещё раньше, чем я планировал."
    "Это всё ещё будет ночь, но какая разница, жизнь [persistent.sayoriname] гораздо важнее."
    "Тогда решено, я вернусь домой и напишу стихотворение."
    "А потом сразу же пойду спать."
    scene bg bedroom with dissolve_scene_full
    "Моя лучшая идея – написать о чувствах, которые я испытываю к клубу."
    "Хорошо."
    scene bg black with dissolve_scene_full
    "Прошло полчаса."
    scene bg bedroomnight with dissolve_scene_full
    "Уже темно... к счастью, успел закончить вовремя."
    "Теперь пора отдохнуть, это необходимо."
    window hide
    pause(1.0)
    scene bg black with dissolve_scene_full
    play music m1
    show monika 2h at t11 zorder 4
    window hide
    pause(0.5)
    "..."
    "Это..."
    show monika 2i at f11 zorder 4
    m "Ты ей не сможешь помочь."
    m "Всё, что ты делаешь, это откладываешь неизбежное!"
    show monika 2h at t11 zorder 4
    mc "Ты серьёзно в это веришь? Я прошёл огромный путь, чтобы сюда добраться."
    mc "Я не позволю, чтобы всё было напрасно, [persistent.sayoriname] не заслуживает депрессии."
    show monika 1i at f11 zorder 4
    m "Она сама в этом виновата, всё было бы хорошо, если бы она просто отпустила тебя."
    show monika 1h at t11 zorder 4
    mc "Нет, ты ошибаешься."
    mc "Я её спасу от этого, и не важно, чего это будет стоить."
    show monika 5c at f11 zorder 4
    m "Я контролирую! Я не дам тебе проснуться вовремя."
    show monika at t11 zorder 4
    mc "Ты забыла о кое о чём, Моника..."
    stop music fadeout 2.0
    pause(3.0)
    mc "Я гораздо сильнее, чем ты."
    scene bg end-glitch3
    window hide
    pause(0.01)
    show screen tear(25, 0.1, 0.1, 0, 60)
    play sound "sfx/glitch1.ogg"
    pause(1.2)
    scene bg black
    hide screen tear
    pause(0.5)
    pause(1.0) #End of Chapter I: My will, my ambition #############################################################################################################################
    scene bg Chapter2 with dissolve_scene_full
    pause(3.0)
    scene bg bedroomnight with dissolve_scene_full
    "..."
    "Времени мало."
    scene bg housenight with wipeleft_scene
    "Я бегу так быстро, как могу."
    scene bg black with dissolve_scene_full
    "Вот коридор!"
    play sound DoorKick
    "Я ворвался в комнату."
    scene bg sayori_bedroom_night
    show sayori 4pvnoose at t11 zorder 4
    window hide
    pause(1.0)
    play music Sayori
    pause(2.0)
    "..."
    "Я был прав..."
    show sayori 4pwnoose at f11 zorder 4
    s "[player]?!"
    show sayori 4pw at t11 zorder 4
    play sound "sfx/fire.ogg"
    "Я снимаю с неё петлю и сжигаю её."
    "Огонь и искры исходят из моей руки..."
    "И слёзы начинают идти из моих глаз..."
    show sayori at f11 zorder 4
    s "[player], я...{nw}"
    show sayori at t11 zorder 4
    mc "Я так старался..."
    show sayori 3pv at t11 zorder 4
    mc "Но... Мне пришлось прибегнуть к крайним мерам."
    mc "[persistent.sayoriname]... почему?"
    show sayori 4pw at f11 zorder 4
    s "Прости меня!"
    s "Я просто..."
    show sayori 4pv at t11 zorder 4
    window hide
    pause(2.0)
    show sayori 1pv at f11 zorder 4
    s "Я никак не могла поверить в то, что ты мне сказал."
    s 2pv "Что-то продолжает мне твердить..."
    show sayori at t11 zorder 4
    "..."
    "Этот взгляд..."
    "Это так больно... гораздо больнее, чем раньше..."
    mc "Несмотря на всё, что я сказал... я не смог изменить ситуацию."
    mc "Как думаешь, почему я захотел проводить с тобой больше времени?"
    mc "Как думаешь, почему я сказал тебе, что ты мне важна?"
    mc "Как думаешь, почему я пришёл сюда так рано?"
    show sayori at f11 zorder 4
    s "..."
    s "Почему?"
    show sayori 1pv at t11 zorder 4
    mc "Потому что я хочу дружить с тобой всю жизнь."
    mc "Я хотел помочь тебе, я хотел не допустить чего-то ужасного с тобой."
    mc "Но в конце концов... это совершенно не важно."
    mc "..."
    mc "[persistent.sayoriname]... есть кое-что, что тебе нужно знать..."
    show sayori 2pv at f11 zorder 4
    s "Д-да?"
    show sayori at t11 zorder 4
    mc "..."
    mc "Я знал, что ты это сделаешь, я знал это уже давно."
    show sayori 1pv at f11 zorder 4
    s "Но... как?"
    show sayori at t11 zorder 4
    mc "Это потому что..."
    window hide
    pause(2.0)
    mc "Я не из этого мира, я не тот человек, которого ты знала."
    mc "И я уже видел, как ты сделала это с собой."
    mc "Вот почему я так не хотел оставлять тебя, я пытался заставить тебя передумать..."
    show sayori at f11 zorder 4
    s "Ч-что ты... несёшь?"
    show sayori at t11 zorder 4
    mc "Я многим пожертвовал после того, как принял это решение."
    mc "В моих амбициях было изменить реальность, не дать тебе покончить с собой."
    mc "Несмотря ни на что... Я сделал это, потому что дорожил тобой."
    show sayori 2pv at f11 zorder 4
    s "[player]... Это всё... правда?"
    show sayori at t11 zorder 4
    mc "Всё до последнего..."
    mc "Извини, я не мог тебе ничего рассказать ранее, ты бы подумала, что это ненормально."
    mc "И..."
    mc "..."
    mc "Ты наверняка не поверила бы мне..."
    show sayori 1pv at f11 zorder 4
    s "Я..."
    s "[player], я не смогу узнать, правда ли это..."
    s 1pzd "Но я..."
    s 2pzd "Я верю тебе."
    show sayori 2pt at t11 zorder 4
    "..."
    mc "Ты... серьёзно веришь тому, что я сказал?"
    show sayori 2pzd at f11 zorder 4
    s "Верю!"
    s "[player]... Ты столько всего сделал для меня за всё это время..."
    s 1pv "Я закрывала глаза на все твои старания, я даже не знала, что могу заслуживать твоей заботы."
    s "Я поступила очень эгоистично, поступив так, я могла разбить тебе сердце..."
    s "Если бы не ты, я бы уже..."
    s "{w=0.5}.{w=0.5}.{w=0.5}."
    s 4pv "Я...{w=1} Я ужасный ч...{nw}"
    show sayori at t11 zorder 4
    mc "Нет."
    show sayori 1pv at t11 zorder 4
    mc "Ты не ужасный человек, [persistent.sayoriname]."
    mc "Ты была под очень сильным давлением, и ты всегда была больна внутри..."
    mc "А ещё... Ты ходила в школу ежедневно, и каждый раз, когда ты была там, там становилось ярче и добрее."
    mc "В этом твоя сила, [persistent.sayoriname]."
    mc "Даже если ты сама так не думаешь."
    show sayori 4pw at f11 zorder 4
    s "Но, [player], я почти покончила с собой!"
    s 1pv "Я очень сильно тебя обидела..."
    show sayori at t11 zorder 4
    mc "[persistent.sayoriname]... Для этого у тебя есть я, помнишь?"
    mc "Я всегда буду на твоей стороне, я тебе обещаю."
    show sayori 2pv at t11 zorder 4
    window hide
    pause(1.0)
    scene bg black with dissolve_scene_full
    "Она подошла ко мне и обняла."
    "Осознание, наконец, доходит до неё, а печаль и гнев внутри меня наконец ушли..."
    s "[player]... Спасибо..."
    s "Ты дал мне причину жить, я никогда не отплачу тебе за это..."
    mc "Ты не должна, [persistent.sayoriname]."
    mc "Но, пожалуйста... Никогда даже не думай о том, чтобы попытаться вновь это сделать."
    s "Не буду... ради тебя."
    "Мы оба свалились с ног, уставшие от слёз."
    "Не говоря ни слова, мы легли спать, в объятиях друг друга."
    stop music fadeout 3.0
    scene bg black with dissolve_scene_full
    window hide
    pause(2.0)
    show monika 1s at f11 zorder 4
    play music m1
    window hide
    pause(1.0)
    m "Почему... Почему не работает?!"
    m "Как она может быть всё ещё жива?!"
    show monika at t11 zorder 4
    mc "Всё кончено, Моника."
    mc "Ты больше никогда не навредишь [persistent.sayoriname]."
    mc "Я об этом позабочусь, помяни моё слово."
    show monika 5c at f11 zorder 4
    m "Ты просто не можешь от неё отстать, да?!"
    m "Это бессмысленно, если ты будешь продолжать так же!"
    show monika at t11 zorder 4
    mc "..."
    mc "Я способен на это."
    show monika 1h at t11 zorder 4
    window hide
    pause(1.0)
    show monika 1i at f11 zorder 4
    m "Ты не можешь всегда поступать по-своему."
    show monika 1h at t11 zorder 4
    mc "У меня не всегда всё шло по-моему."
    mc "Но пока есть что-то, что мне очень дорого... Я никому не позволю уничтожить это по их прихоти."
    mc "Ты больше не увидишь [persistent.sayoriname] так, как раньше, будь уверена."
    stop music fadeout 1.0
    scene bg sayori_bedroom with dissolve_scene_full
    window hide
    pause(1.0)
    "Я замечаю, что [persistent.sayoriname] постепенно просыпается вместе со мной."
    "Забавно, если бы я не поступил так, как поступил, то не увидел бы этого зрелища..."
    mc "[persistent.sayoriname], ты в порядке?"
    show sayori 1pzc at f11 zorder 4
    play music t9
    s "Да... просто чуть-чуть устала, вот и всё."
    show sayori 1pd at t11 zorder 4
    mc "Мы можем не идти в школу, если тебе плохо."
    show sayori 2ph at f11 zorder 4
    s "Нет, я хочу пойти в школу."
    show sayori 2pg at t11 zorder 4
    window hide
    pause(1.5)
    "Вот почему она так сильна, и это ей ещё предстоит понять..."
    mc "Хорошо, а что там со стихотворением?"
    show sayori 1pl at f11 zorder 4
    s "А-а-а... э-э-э... ну, я, э-э-э..."
    show sayori at t11 zorder 4
    mc "Написала что-то, что ты не можешь показать, я прав?"
    show sayori 1ph at f11 zorder 4
    s "Как ты догадался?"
    show sayori at t11 zorder 4
    mc "Подумал и угадал."
    show sayori 1pg at t11 zorder 4
    window hide
    pause(2.0)
    mc "Ничего страшного, [persistent.sayoriname], я тебя понимаю."
    mc "Всё-таки... Я не думаю, что ты хочешь показать это стихотворение им."
    show sayori 1ph at f11 zorder 4
    s "Не хочу!"
    s "Но из-за этого я заставлю тебя ждать."
    show sayori 1pg at t11 zorder 4
    mc "Я не сержусь... мне не сложно подождать, ты знаешь."
    show sayori 1pd at t11 zorder 4
    window hide
    pause(1.0)
    show sayori 1pzc at f11 zorder 4
    s "Ты слишком добрый, [player]."
    s "Я постараюсь справиться как можно быстрее."
    show sayori 1pd at t11 zorder 4
    mc "Не торопись."
    scene bg black with dissolve_scene_full
    "Она заканчивает стихотворение и начинает собираться в школу."
    scene bg residential_day with dissolve_scene_full
    window hide
    pause(1.0)
    show sayori 2g at f11 zorder 4
    s "[player]... как думаешь, всё будет хорошо?"
    show sayori at t11 zorder 4
    mc "Я знаю, что всё будет хорошо, даже если это займёт много времени."
    mc "Будет продолжать болеть, но ты научишься справляться с этим."
    mc "И я сделаю всё, что в моих силах, чтобы вернуть всё на круги своя."
    show sayori 1t at t11 zorder 4
    window hide
    pause(1.0)
    show sayori 1zd at f11 zorder 4
    s "Что бы я без тебя делала..."
    show sayori 1t at t11 zorder 4
    mc "Не думай об этом, [persistent.sayoriname]."
    mc "Готова к школе?"
    show sayori 4s at f11 zorder 4
    s "Агась!"
    scene bg black with dissolve_scene_full
    "После всех этих скучных часов мы вместе пошли в комнату клуба."
    scene bg corridor with dissolve_scene_full
    play music t2
    "Теперь, когда я думаю об этом, мне кажется, это прошло слишком быстро, но как?"
    "Это действительно из-за меня, или из-за Моники?"
    "Мне предстоит выяснить, тем не менее, я считаю, что у Юри скоро начнут проявляться симптомы её проблем."
    show sayori 1h at f11 zorder 4
    s "[player], пока мы не зашли..."
    show sayori 1k at t11 zorder 4
    window hide
    pause(1.0)
    show sayori 2h at f11 zorder 4
    s "Прошу, не рассказывай никому о случившемся."
    show sayori 2g at t11 zorder 4
    mc "С чего бы мне так поступать?"
    mc "Я же не сплетник какой-то."
    show sayori 2d at t11 zorder 4
    window hide
    pause(1.0)
    show sayori 1zc at f11 zorder 4
    s "Спасибо... за всё, что ты делаешь для меня."
    show sayori 1d at t11 zorder 4
    mc "Всё хорошо. Ладно, пойдём, нас ждут."
    scene bg club_day with wipeleft_scene
    window hide
    pause(0.3)
    show sayori 3l at f11 zorder 4
    s "Всем привет... извините, что так опоздали."
    show sayori at t21 zorder 3
    show natsuki 5w at f22 zorder 4
    n "Боже, вам двоим надо лучше планировать своё расписание."
    show natsuki 5y at f22 zorder 4
    n "Я хотела предложить кексы и вам."
    show sayori 4n at f21 zorder 4
    show natsuki at t22 zorder 3
    s "Ты сказала... кексы?"
    show natsuki 4l at f22 zorder 4
    show sayori at t21 zorder 3
    n "Да, я и [player]...{nw}"
    hide sayori with moveoutleft
    n 1e "Эй! Стоять!"
    hide natsuki with moveoutleft
    "[persistent.sayoriname] быстро хватает кексик, прежде чем Нацуки успевает её поймать."
    show sayori 4r at f11 zorder 4
    s "Ура! Есть!"
    show sayori at t21 zorder 3
    show natsuki 5w at f22 zorder 4
    n "Ты так себя по-детски ведёшь, [persistent.sayoriname]."
    show sayori 1q at t31 zorder 3
    show natsuki 5x at t32 zorder 2
    show yuri 2d at f33 zorder 4
    y "Вы обе такие милые!"
    show yuri 2c at t33 zorder 3
    mc "Соглашусь."
    show natsuki 1v at f32 zorder 4
    n "Нет! Никакая я не милая!"
    show sayori at thide zorder 4
    hide sayori
    show yuri at thide zorder 4
    hide yuri
    show natsuki 5w at f11 zorder 4
    n "Угх, почему меня никто всерьёз не воспринимает?!"
    show natsuki 5x at t11 zorder 4
    "Атмосфера из депрессивной превратилась в нечто подобное за считанные минуты, это меня действительно завораживает."
    "Какое же весёлое это место, ха-ха."
    show natsuki 2h at f11 zorder 4
    n "Ладно, где же опять эта Моника?"
    n "Она стала часто опаздывать."
    show natsuki 1g at t11 zorder 4
    "Кто бы догадался... она не очень довольна тем, что у меня тоже есть прозрение."
    "А также тем, что я ей помешал этой ночью."
    mc "Пока мы сюда шли, мы её нигде не видели."
    mc "Ах, а вот и она!"
    show monika 1l at f21 zorder 4
    show natsuki at t22 zorder 3
    m "Извините, ребята! У меня сегодня такой загруженный день."
    show monika 1e at t21 zorder 3
    "Она пялится на [persistent.sayoriname], как и ожидалось."
    show natsuki 5w at f22 zorder 4
    n "Снова загруженный день? Что может быть важнее этого клуба?.."
    show natsuki at t22 zorder 3
    show monika 5b at f21 zorder 4
    m "Ох, прошу, беспокойтесь только о своих проблемах."
    show monika at t21 zorder 3
    show natsuki 1p at f22 zorder 4
    n "Ч-чего?!"
    show natsuki 1o at t22 zorder 3
    show monika 2l at f21 zorder 4
    m "Упс... Извини, Нацуки."
    show natsuki 5g at t22 zorder 3
    show monika 4b at f21 zorder 4
    m "В любом случае, поговорим о задании, что я вам дала вчера..."
    m 2k "Я страстно желаю увидеть ваши произведения!"
    show monika 2a at t21 zorder 3
    "Интересно, что же написали Юри и Нацуки..."
    show natsuki 4y at f22 zorder 4
    n "Вот оно."
    show natsuki 4j at t32 zorder 3
    show monika at t31 zorder 2
    show yuri 4b at f33 zorder 4
    y "А вот моё..."
    show natsuki at thide zorder 4
    hide natsuki
    show yuri at thide zorder 3
    hide yuri
    show monika 1b at f11 zorder 4
    m "Хорошо, у вас есть."
    show monika 1a at t11 zorder 4
    "[persistent.sayoriname] и я достаём свои стихотворения."
    show monika 5a at f11 zorder 4
    m "Никто не забыл, я даже удивлена!"
    m "Я пойду к своему столу и взгляну на ваши стихи."
    show monika at thide zorder 4
    hide monika
    mc "Эй, [persistent.sayoriname]."
    show sayori 4n at f11 zorder 4
    s "Хм?"
    show sayori at t11 zorder 4
    mc "Давай присядем, я хочу тебе кое-что сказать."
    show sayori 2x at f11 zorder 4
    s "Хорошо!"
    scene bg club_day with wipeleft_scene
    window hide
    pause(1.0)
    show sayori 1b at f11 zorder 4
    s "Что ты мне хотел сказать?"
    show sayori at t11 zorder 4
    "Я понизил голос."
    mc "Есть много вещей, которые я тебе хочу рассказать, но я не могу говорить о них здесь."
    mc "Однако, поскольку я не обязан жить в своём доме..."
    mc "У меня идея: я бы мог жить с тобой, если ты не против."
    show sayori 2h at f11 zorder 4
    s "Но... ты уверен?"
    show sayori 2g at t11 zorder 4
    mc "Конечно, не переживай, я не буду скучать по своему дому."
    show sayori 1d at t11 zorder 4
    window hide
    pause(1.0)
    show sayori 4s at f11 zorder 4
    s "Тогда я тебе проведу экскурсию, когда мы туда вернёмся."
    show sayori at t11 zorder 4
    mc "Великолепно! Я думаю, я должен был сделать это раньше..."
    show sayori 1d at t11 zorder 4
    "Тем не менее, это дало мне очередную идею, как я могу помочь Нацуки."
    "Она должна лишь согласиться, но это будет нелегко."
    show sayori 2l at f11 zorder 4
    s "[player], ты делаешь это, чтобы защитить меня?"
    show sayori 2y at t11 zorder 4
    mc "..."
    mc "Ты начинаешь узнавать меня, [persistent.sayoriname]."
    mc "Да... это основная причина, почему я это предложил."
    show sayori 1e at f11 zorder 4
    s "Оу, [player], ты же знаешь, что не обязан."
    show sayori at t11 zorder 4
    mc "Но я хочу этого, я и не хочу, чтобы тебе что-то навредило."
    mc "Это последнее, чего я желаю допустить."
    show sayori 2d at t11 zorder 4
    window hide
    pause(1.0)
    show sayori 4r at f11 zorder 4
    s "Окей, но только, если ты дашь мне и тебя защищать!"
    show sayori at t11 zorder 4
    mc "Ха-ха, ладненько, если ты правда того хочешь."
    show sayori 1a at t11 zorder 4
    "Моника смотрит прямо на нас."
    "Она, должно быть, уже прочла наши стихи..."
    "Теперь, когда я думаю об этом, разве мы не должны были читать стихотворения друг друга?"
    "Видимо, это ещё одно последствие моего пребывания...."
    show sayori 2b at f11 zorder 4
    s "[player], что такое?"
    show sayori at t11 zorder 4
    mc "Ах, извини, мне кажется, Моника дочитала наши произведения."
    show sayori 1x at f11 zorder 4
    s "Ага, давай послушаем, что она скажет!"
    show sayori at thide zorder 4
    hide sayori
    "Моника встаёт из-за стола."
    show monika 2b at f11 zorder 4
    m "Итак, друзья! Вы все хорошо справились с вашими первыми стихами."
    m 5a "Особенно ты, [player], невероятная работа для новенького в клубе."
    show monika at t11 zorder 4
    "..."
    "Что?"
    "Я ожидал, что моя работа будет в её глазах худшей, чего она хочет от меня..."
    show monika 1c at t21 zorder 3
    show natsuki 4d at f22 zorder 4
    n "Дай мне посмотреть!"
    show monika at t31 zorder 2
    show natsuki 4a at t32 zorder 3
    show yuri 2f at f33 zorder 4
    y "Я тоже хочу прочесть."
    show yuri 2e at t33 zorder 2
    show monika 5b at f31 zorder 4
    m "Тише, вы спросите сначала автора, не против ли он!"
    show monika at t31 zorder 3
    mc "Я не против, почему бы и нет?"
    show monika 1c at t31 zorder 2
    "Почему она делает из этого такое событие..."
    "Я даже не написал ничего специфичного для кого-либо."
    "Мне кажется, у неё нет причин так оберегать меня..."
    show monika 1p at f31 zorder 4
    m "Хорошо... Вот."
    show monika 1o at t31 zorder 3
    "Юри и Нацуки вместе приступают к чтению."
    show yuri 1a at t33 zorder 2
    show natsuki 5j at t32 zorder 4
    "По-моему, им нравится, судя по их лицам."
    show natsuki 5d at f32 zorder 4
    n "Неплохо, я ожидала худшего."
    show natsuki 5j at t32 zorder 3
    show yuri 3d at f33 zorder 4
    y "Ты вложил сюда столько чувств, [player]!"
    show yuri 3a at t33 zorder 2
    mc "Я старался, как мог, спасибо."
    show monika 2d at f31 zorder 4
    m "Я заберу её, если вы не запрещаете."
    show monika 2c at t31 zorder 3
    "Она не может отвести от него глаз... ради чего?"
    show yuri 1f at f33 zorder 4
    y "Зачем она тебе так срочно, Моника?"
    show yuri 1e at t33 zorder 3
    show monika 5b at f31 zorder 4
    m "Это не ваше дело!"
    show natsuki 1m at t32 zorder 2
    show monika at t31 zorder 3
    show yuri 3p at f33 zorder 4
    y "Ах!"
    y 4b "И-извини, я просто спросила..."
    show yuri at t33 zorder 4
    window hide
    pause(1.0)
    "В тот момент, когда Юри среагировала, ярость начала стремительно закипать во мне."
    stop music fadeout 2.5
    window hide
    pause(3.0)
    "Мои глаза становятся красными, когда моя злость нарастает..."
    window hide
    pause(2.5)
    show veinmaskb zorder 5: #Aggression scene start
        alpha 0.5
    play music hb
    show layer master at heartbeat
    mc "Чёрт побери, что с тобой такое, Моника?!"
    show yuri 2n at t33 zorder 3
    show natsuki 1p at t32 zorder 2
    show monika 1s at t31 zorder 4
    mc "Почему ты так агрессивна с ними?.. Что они тебе сделали?!"
    mc "С меня хватит..."
    mc "{w=0.5}.{w=0.5}.{w=0.5}."
    mc "!!!"
    stop music fadeout 3.0
    show layer master
    window hide
    pause(2.5)
    hide veinmaskb with dissolve #Aggression scene end
    pause(2.5)
    "Нет... нет! Я не такой!"
    show monika at t41 zorder 1
    show natsuki at t42 zorder 2
    show yuri at t43 zorder 3
    show sayori 4w at f44 zorder 4
    s "[player]?! Что происходит?!"
    play music t9
    mc "Я... Извини, я не думал, что говорил..."
    show natsuki 1n at t42 zorder 2
    show yuri 2w at t43 zorder 3
    show sayori 3v at t44 zorder 4
    window hide
    pause(1.5)
    show sayori at f44 zorder 4
    s "Всё хорошо, [player], я уверена, что Моника хотела сказать не это..."
    show sayori at t44 zorder 4
    show yuri 2t at t43 zorder 3
    mc "Нет! Я... Я просто не хочу, чтобы нечто подобное происходило между нами."
    window hide
    pause(2.5)
    show monika 1g at f41 zorder 4
    m "Юри... Извини, я не хотела тебя обидеть."
    show monika 1f at t41 zorder 1
    show yuri 3zi at f43 zorder 4
    y "Я прощаю тебя, Моника."
    y "У тебя наверняка накапливается много стресса из-за всех твоих дел."
    show yuri 3s at t43 zorder 3
    show sayori 2zc at f44 zorder 4
    s "Моника, ты не должна перетруждать себя работой."
    s "Важно, чтобы ты чувствовала себя хорошо."
    show sayori 2d at t44 zorder 3
    show monika 1n at f41 zorder 4
    m "Нет, я в порядке... Я пойду за стол."
    show natsuki 1j at t42 zorder 3
    m 1e "Спасибо за заботу, друзья, я ценю это."
    show monika at thide zorder 4
    hide monika
    window hide
    pause(1.0)
    show natsuki 4d at f31 zorder 4
    show yuri at t32 zorder 2
    show sayori 1a at t33 zorder 3
    n "Ты меня напугал, [player]."
    n 5c "Я почти точно уверена, что можно было обойтись и без этого."
    n 5d "Моника о нас заботится, поверь."
    show natsuki 5a at t31 zorder 4
    "Если бы я только мог им сказать правду..."
    "Кажется, они не заметили, как мои глаза поменяли цвет."
    "Но это, скорее всего, из-за того, что они не хотят говорить об этом."
    "И как же я им объясню это?.."
    mc "Ладно, я тебе поверю, Нацуки."
    show sayori 2h at f33 zorder 4
    s "[player], можно поговорить наедине?"
    show sayori 2g at t33 zorder 3
    "Она заметила..."
    show yuri 2b at f32 zorder 4
    y "Идите, не волнуйтесь о нас, мы подождём."
    show yuri 1a at t32 zorder 3
    mc "Ох, окей, мы скоро."
    scene bg corridor with wipeleft_scene
    window hide
    pause(1.0)
    show sayori 2h at f11 zorder 4
    s "[player]..."
    show sayori 2g at t11 zorder 4
    window hide
    pause(2.0)
    show sayori 2h at f11 zorder 4
    s "Есть что-то важное, что ты мне не рассказал?"
    show sayori 2g at t11 zorder 4
    mc "..."
    mc "Я ждал подходящего момента, чтобы это обсудить..."
    "И есть ещё много всего, чего я не могу сказать..."
    window hide
    pause(1.0)
    mc "Ты видела это, да?"
    show sayori 1k at t11 zorder 4
    window hide
    pause(1.0)
    show sayori 1h at f11 zorder 4
    s "Ага..."
    s "Почему это с тобой происходит?"
    show sayori 1g at t11 zorder 4
    mc "..."
    mc "Что ж..."
    mc "Я не знаю, как объяснить."
    mc "Когда мои глаза краснеют, это сигнализирует о моей ярости."
    mc "Чем краснее, тем я злее, пока я не..."
    mc "..."
    show sayori 2h at f11 zorder 4
    s "Пока ты... что?"
    show sayori 2g at t11 zorder 4
    mc "Пока я не потеряю сознание."
    show sayori 4w at f11 zorder 4
    s "[player]! Ты должен был мне рассказать, это же серьёзно!"
    show sayori at t11 zorder 4
    mc "Нет! Ты не понимаешь."
    show sayori 1v at t11 zorder 4
    window hide
    pause(1.0)
    mc "Я не допущу такого, [persistent.sayoriname]."
    mc "Я никогда не прощу себя, если сделаю тебе больно."
    mc "Не волнуйся, этого не случится, я уверен."
    show sayori 1u at t11 zorder 4
    window hide
    pause(1.0)
    show sayori 1v at f11 zorder 4
    s "Но... что, если ты причинишь боль другим?"
    show sayori at t11 zorder 4
    mc "..."
    mc "Я пришёл сюда, потому что мне важна ты."
    show sayori 1u at t11 zorder 4
    mc "Мне важен Литературный клуб."
    mc "И я сделаю всё возможное, чтобы не допустить этого."
    show sayori 2v at f11 zorder 4
    s "Как..."
    s "Как ты можешь быть так уверен, что справишься с этим?"
    show sayori 2u at t11 zorder 4
    mc "Потому что..."
    mc "...Я защищаю то, что люблю."
    show sayori 4v at t11 zorder 4
    window hide
    pause(2.0)
    show sayori at f11 zorder 4
    s "[player]..."
    show sayori at t11 zorder 4
    mc "Всё будет хорошо."
    mc "Вот почему я прибыл сюда, никто из вас не заслуживает боли."
    show sayori 1t at t11 zorder 4
    window hide
    pause(1.5)
    show sayori 1zd at f11 zorder 4
    s "Ты прав."
    show sayori 1d at t11 zorder 4
    "Она смахивает слёзы."
    show sayori 2h at f11 zorder 4
    s "Но я не позволю тебе действовать в одиночку."
    s "Я помогу тебе всем, чем смогу."
    show sayori 2g at t11 zorder 4
    mc "..."
    mc "Если ты правда поможешь, то... я не против."
    show sayori 1d at t11 zorder 4
    window hide
    pause(1.0)
    show sayori 1zc at f11 zorder 4
    s "[player]..."
    s "Ты спас меня от смерти..."
    s "Это меньшее, что я могу сделать для тебя."
    show sayori 1d at t11 zorder 4
    mc "Я сделал то, что должен был."
    mc "Пойдём, [persistent.sayoriname], надо вернуться."
    show sayori 2l at f11 zorder 4
    s "Ох, точно... извини за это."
    s 1x "Идём!"
    scene bg club_day with wipeleft_scene
    stop music fadeout 2.0
    window hide
    pause(1.0)
    show monika 1d at t11 zorder 4
    pause(1.5)
    show monika 2b at f11 zorder 4
    play music t2
    m "Я уже собиралась идти искать вас!"  ####
    show monika at t22 zorder 3
    show sayori 5a at f21 zorder 4
    s "Мы задержались слегка больше, чем планировали, извини..."
    show sayori at t21 zorder 3
    show monika 5a at f22 zorder 4
    m "Не переживайте, вы не пропустили ничего важного."
    show sayori 1a at t21 zorder 4
    show monika 2b at t22 zorder 3
    m "Ну ладно, о чём вы двое говорили?"
    show monika 2a at t22 zorder 3
    show sayori 1k at t21 zorder 3
    "Я ожидал, что она проявит любопытство."
    mc "Ничего важного, правда."
    show sayori 2x at f21 zorder 4
    s "Мы просто обсуждали, что будем делать, когда освободимся."
    show sayori 1a at t21 zorder 3
    show monika 1b at f22 zorder 4
    m "Ох, хорошо."
    m 2n "Я хочу передохнуть от работы."
    m "Я ухожу, увидимся завтра на собрании!"
    show monika 1m at t22 zorder 3
    show sayori 2h at f21 zorder 4
    s "Моника! Стой!"
    show monika at thide zorder 4
    hide monika
    "Моника уходит без ответа."
    show sayori 1g at t21 zorder 4
    window hide
    pause(2.0)
    show sayori 2h at f11 zorder 4
    s "[player], как думаешь, с ней всё хорошо?"
    show sayori 2g at t11 zorder 4
    "..."
    "Ей трудно иметь дела со мной."
    "Но если учитывать то, что она видела... Я даже не удивлён."
    mc "Я поговорю с ней завтра."
    show sayori 1d at t11 zorder 4
    window hide
    pause(1.0)
    show sayori 1zc at f11 zorder 4
    s "Спасибо, уверена, она это оценит."
    show sayori 1d at t21 zorder 3
    show yuri 2f at f22 zorder 4
    y "[persistent.sayoriname], [player], я хочу кое-что спросить."
    show yuri 2e at t22 zorder 3
    show sayori 1b at t21 zorder 3
    mc "Да?"
    show yuri 2f at f22 zorder 4
    y "Вы знаете, почему Моника ушла раньше положенного?"
    show yuri 2e at t22 zorder 3
    show sayori 2g at t21 zorder 4
    "..."
    show sayori 2h at f21 zorder 4
    s "Она сказала, что хочет передохнуть от работы.."
    show sayori 2g at t21 zorder 3
    show yuri 3v at f22 zorder 4
    y "Надеюсь, с ней всё хорошо..."
    y "Ситуация, в которую мы попали, должно быть, сильно подействовала на неё."
    show yuri at t22 zorder 4
    mc "Не волнуйтесь, девочки, я разберусь с этим."
    show sayori 1d at t21 zorder 3
    show yuri 3w at t22 zorder 4
    window hide
    pause(1.5)
    show yuri 1b at f22 zorder 4
    y "Я рада, что у нас есть кто-то вроде тебя, [player]."
    show yuri 1a at t22 zorder 3
    mc "Я просто поступаю так, как считаю правильным."
    mc "Ну и потому что я виноват в произошедшем."
    show sayori 2h at f21 zorder 4
    s "Не вини себя, [player]!"
    s "Я понимаю, почему ты разозлился."
    show sayori 2g at t21 zorder 3
    show yuri 2t at f22 zorder 4
    y "Да... это показывает, что ты очень сильно заботишься о нас."
    show yuri 2a at t22 zorder 4
    show sayori 2d at t21 zorder 3
    mc "..."
    mc "Меня успокаивает, что ты понимаешь мои намерения."
    mc "Я хочу просто, чтобы клуб был лучшим местом для всех."
    show sayori 1a at t31 zorder 3
    show yuri 1a at t32 zorder 2
    show natsuki 4z at f33 zorder 4
    n "Ну, мне кажется, это уже лучшее место!"
    n 5c "Если не считать того, что Моника опять переложила мою коллекцию манги."
    show natsuki 5x at t33 zorder 4
    n "Угх... меня это так бесит!"
    mc "Ха-ха... не грусти, Моника не могла положить туда, куда мы не достанем."
    show natsuki 5s at t33 zorder 4
    window hide
    pause(1.0)
    show natsuki 1q at f33 zorder 4
    n "Можешь мне с этим не помогать."
    show natsuki 1d at f33 zorder 4
    n "В общем, пока вас двоих не было, мы с Юри обсуждали, чем могли бы заняться на выходных."
    n "Если у вас нет никаких планов, мы могли бы что-то поделать все вместе."
    show natsuki 1a at t33 zorder 3
    mc "Что думаешь, [persistent.sayoriname]?"
    show sayori 4r at f31 zorder 4
    s "С радостью! Устроим пижамную вечеринку!"
    show sayori at t31 zorder 3
    mc "Я рассчитывал, что ты это скажешь."
    mc "Мы подумаем над этим, девочки."
    show sayori 1a at t31 zorder 3
    show yuri 2f at f32 zorder 4
    y "Нам надо обменяться контактами."
    y "Важно поддерживать друг с другом связь."
    show yuri 2e at t32 zorder 3
    "Это станет небольшой проблемой."
    "Но я почти уверен, что смогу найти тот, который станет моим."
    mc "Да... но у меня его с собой нет, я возьму завтра."
    show yuri 1a at t32 zorder 3
    show natsuki 5c at f33 zorder 4
    n "Только не забудь."
    show natsuki 5g at t33 zorder 2
    mc "Ха-ха... моя память не настолько плоха."
    show natsuki at thide zorder 2
    hide natsuki
    show yuri at thide zorder 3
    hide yuri
    show sayori at thide zorder 4
    hide sayori
    "Мы вернулись на свои места."
    stop music fadeout 2.0
    window hide
    pause(2.0)
    "..."
    "Постепенно мне становится скучно, и я засыпаю."
    scene bg black with dissolve_scene_full
    window hide
    pause(0.5)
    scene bg sayori_bedroom with dissolve_scene_full
    pause(1.0)
    show sayori 2g at t11 zorder 4
    pause(1.0)
    "..."
    "[persistent.sayoriname]...?"
    show sayori 2h at f11 zorder 4
    s "Моника... ч-что ты делаешь?"
    show sayori 2g at t11 zorder 4
    "Подожди... Моника?"
    show vignette zorder 5:
        alpha 0.2
    m "Я просто пришла проведать тебя, [persistent.sayoriname]."
    m "У меня есть то, что тебе нужно."
    "?!"
    "Что происходит?!"
    show sayori 2v at f11 zorder 4
    s "Н-нет..."
    show sayori at t11 zorder 4
    m "Да... это то, что ты хотела, правда?"
    show sayori 4w at f11 zorder 4
    s "Нет! Прекрати, пожалуйста!!"
    scene bg black
    mc "{b}НЕТ{w=0.3}{nw}"
    scene bg end-glitch2
    window hide
    pause(0.01)
    show screen tear(25, 0.1, 0.1, 0, 60)
    play sound "sfx/glitch2.ogg"
    pause(1.0)
    scene bg black
    hide screen tear
    pause(0.01)
    scene bg end-glitch3
    pause(0.01)
    show screen tear(25, 0.1, 0.1, 0, 60)
    play sound "sfx/glitch1.ogg"
    pause(1.0)
    scene bg club_day
    hide screen tear
    pause(2.0)
    show vignette zorder 5:
        alpha 0.6
    play music hb
    show layer master at heartbeat
    pause(3.0)
    "Ч-что я только что...?!"
    show sayori 4w at f11 zorder 4
    s "[player]?!"
    s "Ты в порядке?!"
    show sayori at t11 zorder 4
    "Что... что это должно значить...?"
    window hide
    pause(1.0)
    mc "Я..."
    stop music fadeout 4.0
    window hide
    pause(3.0)
    show layer master
    hide vignette with dissolve
    pause(3.0)
    mc "Со мной всё хорошо, [persistent.sayoriname]."
    show sayori 2v at t11 zorder 4
    window hide
    pause(2.0)
    show sayori at t21 zorder 3
    show yuri 3n at f22 zorder 4
    y "[player], что произошло?"
    show sayori at t31 zorder 3
    show yuri at t32 zorder 2
    show natsuki 1p at f33 zorder 4
    n "Почему ты кричал?!"
    show natsuki at t33 zorder 4
    play music t9
    mc "Я..."
    mc "Я не знаю, будто что-то ужасное происходило передо мной."
    mc "Даже несмотря на то, что это не происходило никогда в прошлом..."
    show yuri 2v at t32 zorder 2
    show sayori at f31 zorder 4
    show natsuki 1n at t33 zorder 3
    s "[player]... с тобой точно всё хорошо?"
    s "Пожалуйста, скажи мне, что тебя беспокоит."
    show sayori at t31 zorder 4
    mc "Нет, [persistent.sayoriname]... ты не понимаешь."
    mc "Ничего страшного, просто кошмарный сон."
    show natsuki 1m at f33 zorder 4
    n "Ты же знаешь, что можешь поговорить с нами об этом, верно?"
    show natsuki at t33 zorder 3
    mc "Конечно, я знаю."
    mc "Это не значит, что я тебе не доверяю."
    mc "Но я не могу втягивать вас во что-то, что не является проблемой..."
    "И как я могу сказать им, что их друг буквально пытается стереть их существование?"
    show yuri 2t at f32 zorder 4
    y "[player], мы всегда с тобой, расскажи нам..."
    show yuri at t32 zorder 2
    mc "..."
    mc "Я видел ужасные вещи, происходящие с тобой."
    "Я указываю на [persistent.sayoriname]."
    mc "И я не хочу, чтобы это когда-нибудь стало реальностью."
    mc "Вы все важны для меня, и я не позволю кому-либо навредить вам."
    show natsuki 1n at t33 zorder 3
    show yuri 2s at t32 zorder 2
    show sayori 1t at t31 zorder 4
    window hide
    pause(1.5)
    show sayori 1zd at f31 zorder 4
    s "[player]..."
    s "Так вот в чём дело..."
    s "Ты беспокоишься о нас."
    show sayori 1t at t31 zorder 3
    mc "Я..."
    mc "..."
    show yuri 2t at f32 zorder 4
    y "Тебе действительно важна судьба клуба..."
    show yuri at t32 zorder 2
    window hide
    pause(1.0)
    mc "Это так, и я хочу, чтобы так оставалось и дальше."
    show natsuki 5d at f33 zorder 4
    n "Боже, ты не должен воспринимать это серьёзно."
    n "Если кто-нибудь попытается связаться с нами, я преподам им должный урок!"
    show sayori 1a at t31 zorder 4
    show yuri 2a at t32 zorder 2
    show natsuki 5a at t33 zorder 3
    mc "Ха-ха... спасибо, Нацуки."
    mc "Я правда ценю это..."
    mc "В любом случае, я думаю, нам пора уходить."
    show sayori 4n at f31 zorder 4
    s "Ох, я совсем забыла про время!"
    s 1x "Тогда, увидимся завтра."
    show sayori 1a at t31 zorder 3
    show natsuki 5c at f33 zorder 4
    n "Не забудь взять с собой телефон, понял?"
    show natsuki at t33 zorder 4
    mc "Не волнуйся об этом, я не забуду."
    window hide
    pause(1.0)
    scene bg corridor with wipeleft_scene
    pause(0.5)
    "Юри и Нацуки идут впереди меня."
    show sayori 2x at f11 zorder 4
    s "Эй, [player], готов идти?"
    show sayori 2a at t11 zorder 4
    mc "Всегда готов!"
    show sayori 1q at t11 zorder 4
    "Она хватает меня за руку и выводит на улицу, полная энергии."
    scene bg residential_day with wipeleft_scene
    "Я просто надеюсь, что она сможет пройти через это."
    "[persistent.sayoriname] дорог{b}а{/b} мне."
    "Несмотря на то, через что мне пришлось пройти, я едва смог понять, как много она значит для меня..."
    show sayori 1b at f11 zorder 4
    s "[player], перед тем, как уйти..."
    s 1l "В моей комнате немного грязно, надеюсь, ты не против."
    show sayori at t11 zorder 4
    mc "Конечно же не против."
    mc "Я помогу убраться тебе позже."
    show sayori 4s at f11 zorder 4
    s "Тогда поторопись!"
    show sayori at thide zorder 4
    hide sayori
    window hide
    pause(0.6)
    scene bg house with wipeleft_scene
    pause(0.6)
    show sayori 1k at t11 zorder 4
    pause(1.0)
    "..."
    mc "[persistent.sayoriname]... ты до сих пор думаешь об этом, не правда ли?"
    show sayori 1h at f11 zorder 4
    s "..."
    s "Как ты-{nw}"
    show sayori at t11 zorder 4
    mc "Это слишком очевидно."
    show sayori 1g at t11 zorder 4
    window hide
    pause(1.5)
    mc "Депрессия оставляет шрам на всю жизнь."
    mc "Но делая то, что ты планировала... это не выход."
    mc "Эта боль переходит к другому человеку, пока он не сделает то же самое."
    show sayori 1g at f11 zorder 4
    s "..."
    s 2h "Как ты... думаешь, что бы сделали другие, если бы я..."
    show sayori at t11 zorder 4
    mc "Я знаю, что они-"
    show sayori 2g at t11 zorder 4
    mc "..."
    mc "Секунду... сейчас, когда я об этом думаю."
    mc "После увиденного, всё вернулось к началу."
    mc "Кроме того... тебя там больше не было, никто даже не знал тебя."
    show sayori 2v at f11 zorder 4
    s "Ч-что...?"
    show sayori at t11 zorder 4
    "Это всё из-за Моники... но я не могу сказать ей это, не сейчас."
    mc "Я сам не очень в этом разбираюсь."
    mc "Но это не важно, ничего из этого никогда не произойдёт."
    show sayori at f11 zorder 4
    s "..."
    s "Почему это происходит с нами?"
    show sayori at t11 zorder 4
    mc "Я... Я не знаю ответа на этот вопрос."
    show sayori 1u at t11 zorder 4
    mc "Это правда сложно, и я не думаю, что ты сможешь что-либо понять из того, что я сказал..."
    mc "Нам следует-"
    show sayori 1b at t11 zorder 4
    "..."
    "Моника...? Что она здесь делает?"
    show sayori at t21 zorder 3
    show monika 2l at f22 zorder 4
    m "Эй, вы двое, простите, что прерываю вас."
    show monika at t22 zorder 3
    show sayori 1l at f21 zorder 4
    s "Привет, Моника, что привело тебя сюда?.."
    show sayori at t21 zorder 3
    show monika 5a at f22 zorder 4
    m "Я шла в библиотеку, не ожидала встретить вас здесь."
    m 2b "О чём вы говорите?"
    show monika 2a at t22 zorder 4
    show sayori 1k at t21 zorder 3
    window hide
    pause(1.5)
    mc "Мы просто... обсуждали проблему."
    show monika 1d at f22 zorder 4
    m "Ох..."
    stop music fadeout 2.0
    window hide
    pause(2.0)
    m "Точно, у [persistent.sayoriname] проблема с депрессией, я почти забыла."
    show sayori 2v at f21 zorder 4
    show monika 1c at t22 zorder 3
    s "..."
    s "М-Моника...?"
    show sayori at t21 zorder 3
    "{w=0.5}.{w=0.5}.{w=0.5}."
    "Что за чёрт?"
    "Почему она так об этом заговорила?!"
    "..."
    "Злость, которую я чувствовал до этого, медленно возвращалась."
    menu:
        "..."
        "Не сдерживаться":
            $ value = 8
        "Защитить [persistent.sayoriname]":
            $ value = 9
        "...":
            $ value = 10
    if value == 8:
        window hide
        pause(3.0)
        show veinmaskb zorder 5: #Aggression scene start
            alpha 0.75
        play music hb
        show layer master at heartbeat
        mc "Слушай внимательно, Моника."
        show monika 1t at t22 zorder 3
        show sayori 4w at t21 zorder 4
        mc "Мне не нравится, как ты с ней обращаешься."
        show screen tear(25, 0.05, 0.05, -20, 80)
        play sound "sfx/glitch2.ogg"
        window hide
        pause(0.1)
        hide screen tear
        mc "Если ты заставишь её чувствовать себя ужасно, я клянусь, что тебе всё вернётся."
        show screen tear(25, 0.05, 0.05, -20, 80)
        play sound "sfx/glitch2.ogg"
        window hide
        pause(0.1)
        hide screen tear
        mc "И я не боюсь-{nw}"
        show sayori at f21 zorder 4
        s "[player]!!"
        s "Пожалуйста, прекрати!"
        show sayori at t21 zorder 4
        mc "{w=0.5}.{w=0.5}.{w=0.5}."
        window hide
        pause(4.0)
        stop music fadeout 2.0
        show layer master
        hide veinmaskb with dissolve
        show sayori 4v at t21 zorder 4
        pause(3.0)
        show monika 1s at t22 zorder 3
        show sayori 2zd at f21 zorder 4
        play music t9
        s "Всё хорошо... [player]."
        s "Монике просто нужно немного времени для себя."
        s "Я понимаю, как тяжело ей приходится."
        show sayori 2t at t21 zorder 3
        window hide
        pause(2.0)
        show monika 1g at f22 zorder 4
        m "П-прости, [persistent.sayoriname]..."
        m "Не знаю, что на меня нашло."
        m 1p "Возможно, для меня будет лучше не идти завтра в клуб."
        show sayori 1g at t21 zorder 4
        show monika 1o at t22 zorder 3
        window hide
        pause(1.5)
        mc "Тебе не обязательно заходить так далеко, Моника."
        mc "Если нужно, отдохни в клубе."
        window hide
        pause(1.0)
        show monika 2n at f22 zorder 4
        m "Я думаю, ты прав..."
        show sayori 1d at t21 zorder 4
        m "Тогда, увидимся завтра в клубе."
        show monika at thide zorder 4
        hide monika
        window hide
        pause(1.5)
        show sayori at t11 zorder 4
        mc "Спасибо, [persistent.sayoriname]..."
        show sayori 2b at f11 zorder 4
        s "За что?"
        show sayori at t11 zorder 4
        mc "За то, что остановила меня, пока всё не вышло из под контроля."
        mc "Я просто не мог этого вынести..."
        show sayori 1zc at f11 zorder 4
        s "Не волнуйся, я понимаю."
        s "Моника должна была заметить это."
        show sayori 1d at t11 zorder 4
        mc "Она – та, кто-"
        show sayori 1b at t11 zorder 4
        mc "{w=0.5}.{w=0.5}.{w=0.5}."
        mc "Неважно, забудь об этом."
        mc "Мы должны идти, пока не стало слишком поздно."
        show sayori 2l at f11 zorder 4
        s "Ох... точно, прости..."
        jump phase4

    if value == 9:
        window hide
        pause(2.0)
        "Я подавляю гнев, который накапливается внутри меня."
        window hide
        pause(1.0)
        mc "Моника, о чём ты говоришь?"
        mc "[persistent.sayoriname] в порядке, мы говорим о другой проблеме."
        show monika 1g at f22 zorder 4
        play music t9
        m "Это правда...?"
        m 2p "Наверное, я что-то недопонимаю, извините за это."
        show monika 2o at t22 zorder 3
        show sayori 1d at t21 zorder 4
        window hide
        pause(1.5)
        show sayori 1zc at f21 zorder 4
        s "Всё в порядке, Моника."
        s "Тебе следует немного отдохнуть, я могу позаботиться о твоей работе за тебя."
        show sayori 1d at t21 zorder 3
        show monika 1y at f22 zorder 4
        m "Я ценю это, но я смогу справиться сама, не волнуйся."
        m 2n "И мне, наверное, пора идти, пока я не забыла об этом."
        show monika 2m at t22 zorder 3
        mc "Тогда, увидимся завтра."
        show sayori 2x at f21 zorder 4
        s "До завтра, Моника!"
        show monika at thide zorder 4
        hide monika
        show sayori 2b at t21 zorder 4
        "Она уходит без дальнейшего ответа."
        window hide
        pause(1.0)
        show sayori 2zc at f11 zorder 4
        s "[player]..."
        s "Спасибо, что так меня защищаешь."
        show sayori 2d at t11 zorder 4
        mc "Эй, помни, что я забочусь о тебе."
        mc "Я не позволю пройти тебе через это одной."
        mc "Так, на чём мы остановились?"
        show sayori 1x at f11 zorder 4
        s "Я хотела показать тебе свой дом, глупышка."
        show sayori 1a at t11 zorder 4
        mc "Конечно!"
        mc "Тогда, пошли."
        jump phase4

    if value == 10:
        window hide
        pause(2.0)
        "С большим трудом мне удаётся противостоять гневу внутри меня."
        mc "{w=0.7}.{w=0.7}.{w=0.7}."
        window hide
        pause(1.5)
        show monika 2n at f22 zorder 4
        m "Подождите... о чём я вообще говорю?"
        m 2m "{w=0.5}.{w=0.5}.{w=0.5}."
        m 1g "Извините за доставленные неудобства."
        show sayori 2v at f21 zorder 4
        show monika 1f at t22 zorder 3
        s "..."
        "[persistent.sayoriname] вытирает свои слёзы."
        show sayori 1zc at f21 zorder 4
        play music t9
        s "Тебе не нужно извиняться, Моника."
        show sayori 2g at f21 zorder 4
        s "Но тебе лучше отдохнуть от работы..."
        show sayori at t21 zorder 4
        mc "Если это будет необходимо, я могу сделать это вместо тебя."
        show sayori 4x at f21 zorder 4
        s "И я тоже могу помочь, мы закончим быстрее таким образом!"
        show sayori 1a at t21 zorder 3
        show monika 1g at f22 zorder 4
        m "Спасибо, ребята."
        m "Но вы не обязаны этого делать, я могу справиться с этим сама."
        show sayori 2g at f21 zorder 4
        show monika 1f at t22 zorder 3
        s "..."
        s 2h "Ты уверена?"
        show sayori 2g at t21 zorder 3
        show monika 2b at f22 zorder 4
        m "Да, в конце концов, я ответственна за это."
        show sayori 1d at t21 zorder 3
        show monika 2a at t22 zorder 4
        mc "Хорошо, но не стесняйся просить у нас помощи."
        mc "Увидимся завтра, Моника."
        show monika 1n at f22 zorder 4
        m "До завтра."
        show monika at thide zorder 4
        hide monika
        show sayori 1b at t21 zorder 4
        "Моника покидает нас в спешке."
        window hide
        pause(2.0)
        show sayori 2h at f11 zorder 4
        s "[player]... почему она ведёт себя так?"
        show sayori 2g at t11 zorder 4
        mc "..."
        mc "Я без понятия, но я сказал тебе, что поговорю с ней."
        mc "И я собираюсь сделать это завтра."
        show sayori 2d at t11 zorder 4
        window hide
        pause(1.5)
        show sayori 4r at f11 zorder 4
        s "Тогда я рассчитываю на тебя!"
        show sayori at t11 zorder 4
        mc "Конечно, давай займёмся делом."
        jump phase4

label phase4:
    scene bg house_corridor with wipeleft_scene
    window hide
    pause(1.0)
    play music t8
    show sayori 1x at f11 zorder 4
    s "Ты уже знаешь, где моя комната, так что я покажу тебе твою."
    s 1l "Раз уж ты собираешься остаться..."
    show sayori 1y at t11 zorder 4
    "Я сразу замечаю, как меняется выражение её лица."
    mc "Ты рада, что я решил это сделать, верно?"
    show sayori at f11 zorder 4
    s "..."
    show sayori 5b at f11 zorder 4
    s "Ты слишком хорошо меня знаешь, [player]."
    s 2zc "Да... когда я с тобой, мне становится лучше."
    show sayori 2d at t11 zorder 4
    mc "Тогда я буду с тобой и помогу тебе преодолеть твои серые тучки."
    mc "Независимо от того, сколько времени это займёт."
    show sayori 2e at f11 zorder 4
    s "{w=0.5}.{w=0.5}.{w=0.5}."
    s 1l "В-в любом случае, в комнате немного грязно."
    s "Я не была здесь долгое время."
    show sayori at t11 zorder 4
    mc "Я не возражаю, уборка – это не проблема."
    show sayori 2x at f11 zorder 4
    s "Тогда за мной!"
    scene bg room2 with wipeleft_scene
    window hide
    pause(0.5)
    show sayori 1l at f11 zorder 4
    s "Надеюсь, тебе будет удобно, это единственная комната, которая у меня есть."
    show sayori at t11 zorder 4
    mc "Здесь вовсе не грязно, я думаю, что привыкну к этому."
    show sayori 4r at f11 zorder 4
    s "Чувствуй себя как дома!"
    s 1l "Буквально..."
    s 2x "Я пойду переоденусь и приготовлю для нас что-нибудь вкусное."
    show sayori 2a at t11 zorder 4
    mc "Конечно, жду с нетерпением!"
    show sayori 4r at f11 zorder 4
    s "Тогда увидимся позже!"
    show sayori at thide zorder 4
    hide sayori
    window hide
    pause(1.0)
    "Мне нужно будет забрать все важные вещи из моей комнаты."
    "Особенно телефон, поскольку в нём есть номер [persistent.sayoriname]..."
    "Пока я этим занимаюсь, я могу поговорить с Нацуки об её предложении."
    "В конце концов, я хочу, чтобы они были счастливы..."
    window hide
    pause(1.0)
    "{w=0.5}.{w=0.5}.{w=0.5}."
    stop music fadeout 4.0
    window hide
    pause(5.0)
    "Это чувство..."
    show screen tear(25, 0.1, 0.1, 0, 60)
    play sound "sfx/glitch2.ogg"
    window hide
    pause(0.3)
    hide screen tear
    "Что оно значит?"
    window hide
    pause(1.0)
    show screen tear(25, 0.1, 0.1, 0, 60)
    play sound "sfx/glitch2.ogg"
    pause(0.6)
    hide screen tear
    pause(2.0)
    "Почему... почему это происходит?"
    if value == 8:
        "Это происходит из-за моих действий?"
    "{w=0.5}.{w=0.5}.{w=0.5}."
    "Возможно, Моника готова сделать ещё один шаг."
    "Если это так, я должен держать ухо востро любой ценой."
    window hide
    pause(1.0)
    scene bg black with dissolve_scene_full
    "После переноса всех предметов в новую комнату..."
    scene bg room2 with dissolve_scene_full
    "Вот, у меня есть всё, что нужно."
    show sayori 2bx at f11 zorder 4
    play music t2
    s "[player]! Еда готова!"
    show sayori 1ba at t11 zorder 4
    mc "Отлично, я только что закончил переносить свои вещи."
    mc "Я больше не могу ждать!"
    show sayori 4br at f11 zorder 4
    s "Тогда поторопись, пока я всё не съела!"
    scene bg living_room with wipeleft_scene
    window hide
    pause(0.5)
    "Мы садимся, расслабляемся и едим вкусную закуску, приготовленную [persistent.sayoriname]."
    show sayori 1bx at f11 zorder 4
    s "[player], у меня есть к тебе просьба."
    s 1bl "Я надеюсь, что ты не возражаешь, но это уже некоторое время не выходит у меня из головы."
    show sayori at t11 zorder 4
    mc "Спрашивай."
    show sayori 1bb at f11 zorder 4
    s "Я удивляюсь..."
    s "Ты сказал мне, что ты не из этого мира."
    s 1bc "Так... как выглядит мир, из которого ты прибыл?"
    show sayori 1bb at t11 zorder 4
    mc "..."
    mc "С чего бы начать...?"
    mc "Ну, он не так уж сильно отличается от этого."
    mc "Но люди там вредят друг другу, они не уважают друг друга."
    show sayori 1bg at t11 zorder 4
    mc "Временами это абсолютный хаос, а что насчёт меня..."
    stop music fadeout 3.0
    mc "{w=0.5}.{w=0.5}.{w=0.5}."
    window hide
    pause(2.0)
    play music t9
    mc "Меня многие боятся и ненавидят, это делает меня своего рода... нежеланным."
    show sayori 2bv at f11 zorder 4
    s "[player]..."
    show sayori at t11 zorder 4
    mc "Ничего, я не принимаю это близко к сердцу."
    show sayori 1bu at t11 zorder 4
    mc "Они ничего не могут мне сделать."
    mc "И поскольку я был тем, кто лучше всех защищал свой город, я заслужил уважение большинства людей."
    mc "Но некоторые из этих людей боятся меня и, вероятно, хотят избегать."
    show sayori at f11 zorder 4
    s "..."
    s 2bh "Я понятия не имела..."
    s "[player], тебе следовало сказать мне об этом раньше!"
    show sayori 2bg at t11 zorder 4
    mc "Поверишь ли ты в это?"
    show sayori 2bk at t11 zorder 4
    window hide
    pause(2.0)
    show sayori 1bh at f11 zorder 4
    s "Ты уже рассказал другим девушкам?"
    show sayori 1bg at t11 zorder 4
    mc "Только ты об этом знаешь."
    mc "Но я расскажу им, рано или поздно."
    mc "Не волнуйся, я знаю, что делаю, можешь доверять мне."
    show sayori at f11 zorder 4
    s "{w=0.5}.{w=0.5}.{w=0.5}."
    s 2bh "[player], я могу помочь."
    show sayori at t11 zorder 4
    mc "Нет."
    show sayori 1bg at t11 zorder 4
    window hide
    pause(2.0)
    mc "[persistent.sayoriname]... я не из тех, кому нужна помощь."
    mc "Кроме того, возможность проводить время с тобой уже делает мой день лучше."
    show sayori 1bd at f11 zorder 4
    s "..."
    show sayori 1bzc at f11 zorder 4
    s "Я правда рада, что это делает тебя счастливее."
    s 2bh "Но ты должен сказать мне, если тебе будет грустно."
    s "Твоё счастье тоже важно!"
    show sayori 2bg at t11 zorder 4
    mc "Я ценю твою заботу, но я уже честен с тобой."
    mc "Зачем мне скрывать от тебя свои чувства?"
    mc "Я доверяю тебе, [persistent.sayoriname]."
    show sayori 1bd at t11 zorder 4
    window hide
    pause(2.0)
    show sayori 2bc at f11 zorder 4
    s "[player], есть ещё одна вещь, о которой я хочу знать."
    s "Когда..."
    show sayori 1bk at f11 zorder 4
    s "..."
    s 1bh "Когда ты пришёл ко мне той ночью..."
    s "Ты сжёг петлю, но я не видела, чтобы ты использовал зажигалку."
    show sayori 1bg at t11 zorder 4
    "Что?"
    "Как я мог использовать зажигалку? Было слишком много огня, чтобы это оказалось правдой."
    "Но сейчас нет причин что-либо скрывать, она заслуживает того, чтобы знать."
    mc "Ну... дело в том, что..."
    mc "Я не использовал зажигалку."
    show sayori 1bb at t11 zorder 4
    window hide
    pause(1.0)
    show sayori 2bc at f11 zorder 4
    s "Но..."
    s "Как ты это сделал?"
    show sayori 2bb at t11 zorder 4
    mc "Я..."
    mc "Ну, понимаешь..."
    mc "Я могу{w=0.5}.{w=0.5}.{w=0.5}. манипулировать стихиями."
    show sayori 4bh at f11 zorder 4
    s "Ч-что?"
    show sayori 4bg at t11 zorder 4
    mc "Я объясню..."
    show sayori 1bg at t11 zorder 4
    mc "Большинство людей из моего мира способны использовать сверхъестественные силы."
    mc "Это звучит действительно невообразимо, но именно так я смог войти в ваш мир."
    mc "Пока лишь немногие из нас способны путешествовать в другие измерения."
    mc "Я даже не могу считать это безопасным, это отнимает много энергии..."
    show sayori 1bg at f11 zorder 4
    s "..."
    s 2bv "Почему ты рисковал жизнью ради меня?"
    show sayori at t11 zorder 4
    mc "Я сильнее этого, [persistent.sayoriname]."
    mc "Я не позволю этому остановить меня."
    window hide
    pause(1.5)
    show sayori at f11 zorder 4
    s 2bv "А что насчёт твоих друзей?"
    s 4bv "Должно быть, они скучают по тебе..."
    show sayori at t11 zorder 4
    mc "Да, вероятнее всего."
    mc "Но они понимают, это было моё желание всё исправить."
    show sayori 2bt at t11 zorder 4
    window hide
    pause(1.5)
    show sayori 2bzd at f11 zorder 4
    s "Ты делаешь всё, что в твоих силах, для нашего клуба."
    s "Не слушай, что думают о тебе эти подлые люди, которые тебя ненавидят."
    s "Злой человек никогда бы не сделал что-то подобное для нас."
    show sayori 1bt at t11 zorder 4
    "Она понимает мои намерения, чего все остальные не могли сделать всё это время..."
    window hide
    pause(2.0)
    mc "Спасибо, [persistent.sayoriname]."
    show sayori 1bb at f11 zorder 4
    s "М-м-м?"
    show sayori at t11 zorder 4
    mc "Ты дала мне всё, в чём я нуждался."
    mc "Вот почему я не хочу, чтобы ты думала о себе, как об эгоисте."
    mc "Потому что ты не эгоистична совсем."
    mc "Может показаться, что ты даёшь мне не так уж много, но это не так."
    mc "Так что, пожалуйста, не говори, что ты эгоистка..."
    show sayori 1bd at t11 zorder 4
    window hide
    pause(2.0)
    scene bg black with dissolve_scene_full
    pause(1.0)
    "Она подходит и обнимает меня."
    window hide
    pause(1.0)
    s "Если это то, что ты хочешь..."
    s "..."
    s "Тогда я не буду считать себя эгоистичным человеком."
    mc "{w=0.5}.{w=0.5}.{w=0.5}."
    "Я больше не мог формулировать слова."
    "Это чувство, которое я испытываю к ней... Я его не понимаю..."
    window hide
    pause(2.0)
    mc "Всякий раз, когда тебе будет плохо, не стесняйся приходить и говорить со мной об этом."
    mc "Я помогу тебе пройти через это, чего бы это ни стоило."
    mc "Потому что видеть, как тебе становится лучше, – это всё, о чём я мог просить..."
    s "Я не смогла бы стать лучше без тебя."
    s "...{w=1.5}Я люблю тебя."
    scene bg black with dissolve
    window hide
    pause(0.5)
    scene bg living_room with dissolve_scene_full
    pause(2.0)
    show sayori 2bt at t11 zorder 4
    pause(1.0)
    "Это именно то, что я чувствую?.."
    "Несмотря на все мои давние мысли и сомнения, так ли это на самом деле должно быть?"
    mc "..."
    mc "Я тоже люблю тебя, [persistent.sayoriname]."
    window hide
    pause(2.0)
    show sayori 1bb at f11 zorder 4
    s "[player], я только что подумала кое о чём."
    s 3bc "Что ты будешь делать со своим домом?"
    show sayori 3bb at t11 zorder 4
    mc "Я думал об этом некоторое время назад."
    mc "Лучшее, что я мог бы сделать, это отдать его Нацуки."
    show sayori 1bb at f11 zorder 4
    s "..."
    s 1bc "Нацуки?"
    show sayori 1bb at t11 zorder 4
    mc "Да, для этого есть причины."
    mc "Но тебе не нужно беспокоиться об этом."
    mc "Я пойду поговорю с ней, когда найду подходящее время."
    show sayori 2bl at f11 zorder 4
    s "Она, скорее всего..."
    show sayori at t11 zorder 4
    mc "Не позволит мне сделать это для неё, верно?"
    show sayori 1bb at t11 zorder 4
    window hide
    pause(1.0)
    show sayori 1bc at f11 zorder 4
    s "Ты быстро учишься, это очевидно."
    show sayori 1bb at t11 zorder 4
    mc "Я знаю, но это не главная причина, почему я знаю."
    mc "Это потому, что я уже видел ваши личности раньше."
    show sayori at f11 zorder 4
    s "Оу..."
    s 1bl "Верно, я забыла..."
    s 1bx "Но я уверена, что ты заставишь Нацуки согласиться."
    s 4br "Я верю в тебя, [player]!"
    show sayori at t11 zorder 4
    "Её улыбка такая милая, она всегда согревает моё сердце..."
    mc "Я тебя не подведу."
    show sayori 1ba at t11 zorder 4
    mc "Хочешь посмотреть фильм вместе?"
    show sayori 2bx at f11 zorder 4
    s "С удовольствием!"
    s "Есть что-то особенное, что бы ты хотел посмотреть?"
    show sayori 2ba at t11 zorder 4
    mc "Мы могли бы посмотреть аниме, в котором много экшена."
    show sayori 2bb at t11 zorder 4
    window hide
    pause(1.5)
    show sayori 2bl at f11 zorder 4
    s "Я не ожидала услышать это от тебя."
    s 1bc "Не пойми меня неправильно, я не против аниме."
    s 3bx "Посмотрим, что мы сможем найти."
    scene bg black with dissolve_scene_full
    window hide
    pause(1.0)
    "Время проходит незаметно, пока мы вместе смотрим аниме."
    window hide
    pause(2.0)
    scene bg living_room_late with dissolve_scene_full
    pause(1.0)
    show sayori 1bb at t11 zorder 4
    "Мы почти теряем счёт времени."
    show sayori 1bc at f11 zorder 4
    s "[player], становится поздно."
    s "Я думаю, что пойду отдохну."
    show sayori 1bb at t11 zorder 4
    mc "Я пока не буду спать, я привык ложиться позже."
    show sayori 2bh at f11 zorder 4
    s "Но не задерживайся!"
    show sayori 2bg at t11 zorder 4
    mc "Не волнуйся об этом, я буду следить за временем."
    show sayori 1bd at t11 zorder 4
    window hide
    pause(2.0)
    show sayori 4bx at f11 zorder 4
    s "Хорошо, спокойной ночи!"
    show sayori 1ba at t11 zorder 4
    mc "Спокойной ночи, [persistent.sayoriname]."
    show sayori at thide zorder 4
    hide sayori
    window hide
    pause(2.0)
    "Что мне стоит делать дальше..."
    "Что-то подсказывает мне, что Моника завтра не придёт в клуб."
    if value == 8:
        "Я был немного груб с ней, я не могу её винить."
        "С другой стороны, она знает, что нельзя так разговаривать с [persistent.sayoriname]."
    "В любом случае, мне придётся поговорить с ней наедине."
    "Даже если ей это не понравится."
    "В худшем случае..."
    "{w=0.5}.{w=0.5}.{w=0.5}."
    window hide
    stop music fadeout 3.0
    pause(4.0)
    "{cps=20}Мне нужно поговорить с ней по-плохому.{/cps}"
    show screen tear(25, 0.1, 0.1, 0, 60)
    play sound "sfx/glitch2.ogg"
    window hide
    pause(0.6)
    hide screen tear
    pause(1.5)
    "О чём я думаю? Я пришёл сюда помочь им всем."
    "Я пришёл сюда, чтобы показать Монике, что она не должна делать ничего из того, что она делает."
    "..."
    "Мне следует отправиться в свою комнату."
    window hide
    pause(1.0)
    scene bg black with dissolve_scene_full
    "После подготовки к завтрашнему дню..."
    window hide
    pause(0.1)
    scene bg room2_night with dissolve_scene_full
    "Для меня необычно рано идти отдыхать."
    "Я думал, разница во времени будет не такой уж большой."
    "Но я должен был ожидать этого после попадания в другой мир."
    "Даже если он предположительно похож на мой..."
    "Ну... я думаю, завтра всё будет в порядке."
    window hide
    pause(1.0)
    scene bg black with dissolve_scene_full 
    pause(1.0) #End of Chapter 2: Importance in realization ########################################################################################################################
    scene bg Chapter3 with dissolve_scene_full
    pause(3.0)
    scene bg black with dissolve_scene_full
    "Это была спокойная ночь без каких-либо кошмаров или видений."
    "Моника тоже не пыталась завязать разговор."
    window hide
    pause(2.0)
    scene bg room2 with dissolve_scene_full
    pause(1.0)
    "Я медленно просыпаюсь и начинаю слышать шаги за пределами моей комнаты."
    "Кто-то стучит в дверь, это, скорее всего, [persistent.sayoriname]."
    mc "Да?"
    "Она входит в комнату."
    play music t8
    show sayori 4bs at f11 zorder 4
    s "Э-э-э-э-эй!"
    s 2bx "Просыпайся, соня! Скоро мы пойдём в школу."
    show sayori 2ba at t11 zorder 4
    mc "Я уже проснулся, но в любом случае, спасибо тебе."
    show sayori 1br at f11 zorder 4
    s "Смотри, кто из нас сейчас проспал."
    s 2bx "Пойдём, я кое-что приготовила для тебя!"
    show sayori 1ba at t11 zorder 4
    mc "Хорошо, уже иду."
    scene bg living_room with wipeleft_scene
    pause(1.0)
    "Когда я вхожу в гостиную, я замечаю много еды на столе."
    "Это почти похоже на праздник."
    show sayori 4br at f11 zorder 4
    s "Я приготовила отличный завтрак для нас!"
    show sayori at t11 zorder 4
    mc "..."
    mc "Э-хе-хе... как мне... описать это?"
    show sayori 2bn at f11 zorder 4
    s "М-м-м?"
    show sayori at t11 zorder 4
    mc "Я правда ценю, что ты сделала."
    mc "Но я..."
    mc "..."
    mc "Я не завтракаю."
    show sayori 2bz at f11 zorder 4
    s "Ч-что?!"
    s 4bp "Это неприемлемо, [player]!"
    s 4bz "Ты должен кушать по утрам! Это важно для твоего здоровья!"
    show sayori at t11 zorder 4
    mc "Ладно, ладно, я... попробую."
    show sayori 4bg at t11 zorder 4
    mc "Но на самом деле я не голоден, поэтому ничего не обещаю."
    show sayori 2bd at t11 zorder 4
    window hide
    pause(2.3)
    show sayori 2br at f11 zorder 4
    s "Всё в порядке, съешь сколько сможешь!"
    scene bg black with dissolve_scene_full
    "Мы завтракаем вместе, и, несмотря на отсутствие интереса к нему, я как-то умудрился съесть достаточно."
    "[persistent.sayoriname] поражает меня..."
    window hide
    pause(2.0)
    scene bg living_room with dissolve_scene_full
    "Уже почти пора идти в школу."
    mc "Эй, [persistent.sayoriname]."
    show sayori 2bb at f11 zorder 4
    s "Хм?"
    show sayori at t11 zorder 4
    mc "Как ты думаешь, Моника собирается прийти?"
    show sayori 2bk at f11 zorder 4
    s "..."
    s 1bh "Я правда не знаю, но я надеюсь, что она будет."
    if value == 8:
        s 2bh "Возможно, она чувствует себя напуганной после вчерашнего..."
        show sayori 2bg at t11 zorder 4
        mc "..."
        mc "Возможно, это будет нелегко, но я постараюсь наверстать упущенное."
    show sayori 1bg at t11 zorder 4
    window hide
    pause(2.0)
    mc "Если она не появится, тогда я спрошу её лично."
    mc "Но мы должны получить контакты Юри и Нацуки."
    show sayori 1bc at f11 zorder 4
    s "Ох, конечно!"
    s 1bl "Я почти забыла об этом."
    s 2bx "Ладно, я пойду оденусь, подожди меня здесь."
    show sayori at thide zorder 4
    hide sayori
    window hide
    pause(2.0)
    "Кто знает, что ещё мне придётся решить."
    "Сейчас всё станет ещё более напряжённым, я должен подготовиться."
    scene bg black with dissolve_scene_full
    "Мы вместе идём в школу и быстро заканчиваем занятия."
    scene bg corridor with dissolve_scene_full
    "Я вижу Нацуки, стоящую перед дверью комнаты."
    "Она выглядит... расстроенной?"
    mc "Нацуки?"
    "Нацуки бежит к нам."
    show natsuki 1m at f11 zorder 4
    n "Я так рада, что вы здесь."
    n "Есть кое-что очень важное, что вы должны увидеть."
    show natsuki 1n at t11 zorder 4
    "Она протягивает нам листок бумаги."
    stop music fadeout 4.0
    call showpoem(poem_m5, music=False) from _call_showpoem_1
    mc "..."
    mc "Я ожидал этого."
    show natsuki at t21 zorder 3
    show sayori 2v at f22 zorder 4
    s "[player]..."
    show sayori at t22 zorder 3
    mc "Всё в порядке, я пойду поговорю с ней, но перед этим мы должны обменяться номерами телефонов."
    show natsuki 2m at f21 zorder 4
    n "Мы можем сделать это позже, иди и поговори с Моникой, это важнее."
    show natsuki at t21 zorder 3
    mc "..."
    mc "Я полагаю, ты права."
    mc "Я скоро вернусь, берегите себя!"
    scene bg residential_day with wipeleft_scene
    "Где я могу найти Монику?"
    "{w=0.5}.{w=0.5}.{w=0.5}."
    "Я должен усилить своё внимание, таким образом, я могу начать чувствовать её присутствие."
    "Она должна быть где-то рядом..."
    play sound Glow
    window hide
    pause(3.0)
    "Я начал чувствовать её присутствие рядом со мной."
    "Туда!"
    scene bg house2 with wipeleft_scene
    "Она внутри этого дома."
    "Я звоню в дверь."
    "..."
    "Она выходит наружу."
    show monika 2bd at t11 zorder 4
    window hide
    pause(2.0)
    play music t10
    mc "Привет, Моника, ты в порядке?"
    show monika 1bo at f11 zorder 4
    m "{w=0.5}.{w=0.5}.{w=0.5}."
    m 1bp "Зачем ты пришёл сюда, что тебе нужно?"
    show monika 1bo at t11 zorder 4
    mc "Они хотят, чтобы ты была с ними, ты знаешь."
    mc "Смотри..."
    mc "Я знаю, что я, вероятно, последний, кого ты хочешь сейчас видеть."
    mc "Но всё, что я делаю, это пытаюсь помочь им справиться с их проблемами."
    mc "И я хочу помочь тебе тоже."
    show monika 1bg at f11 zorder 4
    m "..."
    show monika at t11 zorder 4
    pause(2.0)
    show monika 1br at f11 zorder 4
    m "Что изменится, если я уйду?"
    m 2bp "Видеть, как ты просто разговариваешь с другими... причиняет мне боль."
    show monika 2bo at t11 zorder 4
    mc "И ты думаешь, что запереться – это единственный способ решить эту проблему?"
    mc "Они все скучают по тебе, и я знаю, что ты всё ещё хочешь быть там, где-то глубоко в своих мыслях."
    show monika 1bg at t11 zorder 4
    window hide
    pause(2.5)
    show monika 1br at f11 zorder 4
    m "Ладно..."
    m 1bp "Просто дай мне немного времени..."
    show monika 1bo at t11 zorder 4
    mc "Я буду ждать тебя здесь."
    show monika at thide zorder 4
    hide monika
    window hide
    pause(1.5)
    "Я знал, что она будет бороться, она не может использовать свои силы, чтобы манипулировать этим миром."
    "По крайней мере, не тогда, пока я здесь..."
    "Сможет ли она вообще справиться с этим по-другому?.."
    "..."
    "Ей придётся, я не позволю ей причинять вред другим только ради неё самой."
    window hide
    pause(2.0)
    show monika 2bg at f11 zorder 4
    m "Я готова..."
    show monika 2bf at t11 zorder 4
    mc "Тогда идём, все ждут нас."
    scene bg residential_day with wipeleft_scene
    pause(1.0)
    "Мы вместе идём в школу."
    "Я заметил, как она держится подальше от меня."
    "Но в то же время, кажется, что она хочет быть со мной."
    "Это сбивает с толку, что она на самом деле думает обо мне?"
    window hide
    pause(1.0)
    scene bg corridor with wipeleft_scene
    "Мы подходим к двери."
    "Моника остаётся немного позади."
    mc "Что-то не так, Моника?"
    show monika 2bo at f11 zorder 4
    m "..."
    m 2bp "Что я должна сказать им?"
    show monika 2bo at t11 zorder 4
    mc "Просто скажи им, что ты передумала."
    mc "Они будут рады, что ты здесь, объяснения не важны."
    show monika 1br at f11 zorder 4
    m "Ты уже настолько хорошо их знаешь..."
    show monika 1bq at t11 zorder 4
    mc "..."
    mc "Ну же, давай больше не будем тратить время впустую."
    window hide
    pause(1.0)
    scene bg club_day with wipeleft_scene
    m "Всем привет, я вернулась!"
    show sayori 2b at t33 zorder 4
    show yuri 1e at t32 zorder 3
    show natsuki 1k at t31 zorder 2
    "Все они быстро встают и подходят ближе."
    "Я рад, что мне удалось убедить Монику, они бы уже были разочарованы..."
    show monika 2bn at f41 zorder 4
    show sayori 2x at t44 zorder 3
    show natsuki 5j at t42 zorder 1
    show yuri 1c at t43 zorder 2
    m "П-привет..."
    show monika 2bm at t41 zorder 3
    show sayori 4r at f44 zorder 4
    s "Моника!"
    s 2zc "Я думала, что ты больше не вернёшься..."
    show sayori 2d at t44 zorder 3
    show yuri 2f at f43 zorder 4
    show monika 2bo at t41 zorder 1
    y "Моника, если тебя что-то беспокоит, ты всегда можешь поговорить с нами об этом."
    y 1d "Не бойся открыться нам."
    show yuri 1a at t43 zorder 2
    show monika 2bf at f41 zorder 4
    m "{w=0.5}.{w=0.5}.{w=0.5}."
    m 2bg "Ребята, мне правда не нужна помощь."
    show monika at thide zorder 4
    hide monika
    show yuri 1e at t43 zorder 3
    show sayori 1g at t44 zorder 4
    show natsuki 2n at t42 zorder 2
    "Моника торопливо направляется к своему столу."
    window hide
    pause(2.0)
    show yuri 1e at t32 zorder 3
    show sayori 2h at f33 zorder 4
    show natsuki 2n at t31 zorder 2
    s "[player], что с ней произошло?"
    show sayori 2g at t33 zorder 4
    mc "Она..."
    window hide
    pause(2.0)
    mc "Ей нужно время побыть одной."
    mc "Поверь мне, я докопаюсь до сути."
    show sayori 4h at f33 zorder 4
    s "Нет, ты не можешь делать это в одиночку!"
    s "Это кажется большой проблемой..."
    show sayori 4g at t33 zorder 3
    show natsuki 5d at f31 zorder 4
    n "Да, мы все хотим лучшего для Моники."
    n 5c "Так что не пытайся взвалить это на себя."
    show sayori 1d at t33 zorder 3
    show yuri 1a at t32 zorder 2
    n 2z "Я уверена, что мы сможем придумать что-нибудь, чтобы подбодрить её."
    show natsuki at t31 zorder 4
    mc "..."
    mc "У меня есть идея."
    show sayori 1b at t33 zorder 3
    show natsuki 2k at t31 zorder 4
    show yuri 1e at t32 zorder 2
    mc "Помните, что мы планировали?"
    mc "Как насчёт того, чтобы пригласить её? Я почти уверен, что она это оценит."
    show yuri 2c at t32 zorder 2
    show natsuki 5j at t31 zorder 3
    show sayori 4r at hf33 zorder 4
    s "Это отличная идея!"
    show sayori at t33 zorder 3
    show yuri 2d at f32 zorder 4
    y "Мы могли бы приготовить для неё что-нибудь особенное."
    show sayori 1a at t33 zorder 3
    y 1b "Я могу дать ей почитать книгу и приготовить чай."
    show yuri 1a at t32 zorder 2
    show natsuki 4z at f31 zorder 4
    n "Я сделаю много кексов, она не сможет отказаться!"
    show natsuki at t31 zorder 3
    show sayori 2x at f33 zorder 4
    s "И я выполню всю её работу."
    show natsuki 2j at t31 zorder 3
    show sayori 2a at t33 zorder 4
    mc "Отлично, а я..."
    window hide
    pause(2.0)
    mc "Ей нужно с кем-то поговорить, и это именно то, что я могу для неё сделать."
    mc "Особенно, если она такая, потому что чувствует себя одинокой."
    show natsuki 1d at f31 zorder 4
    n "Отлично! Тогда давайте обменяемся номерами телефонов."
    scene bg black with dissolve_scene_full
    "Пока мы обмениваемся нашими контактами, я замечаю, что Моника пристально смотрит на нас."
    "Такое ощущение, будто она расстроена этим..."
    scene bg club_day with dissolve_scene_full
    play music t2
    show yuri 1c at t32 zorder 2
    show natsuki 2j at t31 zorder 3
    show sayori 2x at f33 zorder 4
    s "Хорошо, я напишу вам всем завтра, мы встретимся у моего дома."
    show sayori 1a at t33 zorder 3
    show yuri 1b at f32 zorder 4
    y "Хорошо, я вернусь к чтению, скажите мне, если я понадоблюсь."
    show yuri at thide zorder 4
    hide yuri
    window hide
    pause(1.5)
    show natsuki 2d at f21 zorder 4
    show sayori at t22 zorder 3
    n "О, и не волнуйтесь, я оставлю вас двоих наедине."
    show sayori 1b at t22 zorder 3
    n 5d "Я уже знаю, что вы двое близки друг другу."
    show sayori 4q at t22 zorder 4
    show natsuki 5z at t21 zorder 3
    mc "Ч-что?!"
    show natsuki at thide zorder 3
    hide natsuki
    "Нацуки быстро уходит."
    window hide
    pause(2.0)
    show sayori 2x at f11 zorder 4
    s "Да ладно тебе, [player], нельзя с этим не согласиться!"
    s 4s "Хе-хе..."
    show sayori at t11 zorder 4
    mc "..."
    mc "Конечно нет."
    show sayori 1d at t11 zorder 4
    mc "Но это правда так очевидно?"
    mc "Не то, чтобы это имело значение, это не меняет того, что я думаю о тебе."
    show sayori 2d at t11 zorder 4
    stop music fadeout 4.0
    window hide
    pause(3.0)
    "Она подходит ближе."
    play music t9
    show sayori 2zd at f11 zorder 4
    s "Я правда счастлива за всё то, что ты сделал для меня."
    s 4zd "Я так тебя люблю, [player]."
    show sayori 4t at t11 zorder 4
    window hide
    pause(2.0)
    "Когда она говорит это, я притягиваю её ближе к себе."
    mc "Я тоже люблю тебя, [persistent.sayoriname]."
    show sayori at thide zorder 4
    hide sayori
    "Мы обнимаем друг друга, чувствуя комфорт."
    "Но внезапно Моника встает и быстро подходит к нам, как будто она хотела бы, чтобы мы разделились."
    show monika 2bi at f11 zorder 4
    m "..."
    show monika 2bo at t21 zorder 3
    show sayori 1b at t22 zorder 4
    "[persistent.sayoriname] и я оборачиваемся, ожидая, что Моника что-то скажет."
    show sayori 2c at f22 zorder 4
    s "Моника? Тебе что-то нужно от нас?"
    show sayori 2b at t22 zorder 3
    show monika 1bf at t21 zorder 4
    "Она молчит, глядя прямо на [persistent.sayoriname]."
    window hide
    pause(2.0)
    show monika 2bp at f21 zorder 4
    m "Извините, ничего особенного."
    show sayori 2g at t22 zorder 3
    m "Я..."
    show monika 2bo at t21 zorder 4
    mc "Эй, Моника, я хотел рассказать тебе кое о чём, что мы придумали."
    show monika 2bc at t21 zorder 4
    mc "Как насчёт того, чтобы ты завтра пришла на нашу встречу?"
    show sayori 1q at t22 zorder 3
    mc "Мы будем смотреть фильмы, есть много еды и отлично проведём время вместе."
    show monika 1bo at f21 zorder 4
    m "{w=0.5}.{w=0.5}.{w=0.5}."
    m 1bp "Я подумаю над этим..."
    show monika 1bo at t21 zorder 3
    show sayori 4h at f22 zorder 4
    s "Давай, Моника! Тебе понравится!"
    s 4r "Не беспокойся о работе, я могу позаботиться об этом вместо тебя."
    show sayori at t22 zorder 3
    show monika 1bf at t21 zorder 4
    window hide
    pause(2.0)
    show monika 1bw at t21 zorder 4
    "Как только [persistent.sayoriname] говорит это, из глаз Моники текут слёзы."
    "По моим догадкам, прямо сейчас она испытывает чувство вины и сожаления."
    "Все это время она пыталась причинить боль [persistent.sayoriname], и то, что она пытается сделать для неё что-то приятное, должно было как-то повлиять на её чувства."
    window hide
    pause(2.0)
    show monika 1bx at f21 zorder 4
    m "Почему ты сделала это для меня?"
    show monika 1bw at t21 zorder 3
    show sayori 2x at f22 zorder 4
    s "Глупая Моника, ты слишком много работаешь! Ты заслуживаешь возможности отдохнуть!"
    s 2h "Пожалуйста, пойдём с нами, мы действительно хотим, чтобы ты была там."
    show sayori 2g at t22 zorder 3
    show monika 1bo at t21 zorder 4
    window hide
    pause(2.5)
    show monika 2bg at f21 zorder 4
    m "Ладно... Я думаю, я могла бы прийти."
    show monika 2bf at t21 zorder 3
    show sayori 4r at f22 zorder 4
    s "Ура!"
    s 2x "Я напишу тебе завтра, хорошо?"
    show sayori 2a at t22 zorder 3
    show monika 1bp at f21 zorder 4
    m "Хорошо..."
    show monika at thide zorder 4
    hide monika
    "Моника возвращается к своему столу."
    "Несмотря на то, как она вела себя и что она сделала, я верю, что она может измениться, по крайней мере, если попытается..."
    show sayori 4r at f11 zorder 4
    s "Мы должны сделать этот день приятным для неё!"
    show sayori 1d at t11 zorder 4
    mc "Просто нужно убедиться, что она появится."
    mc "Без паники, я позабочусь об этом!"
    show sayori 2q at t11 zorder 4
    window hide
    pause(2.0)
    show sayori 2b at f11 zorder 4
    s "[player], я почти забыла сказать тебе."
    s 1c "Нацуки хочет поговорить с тобой, она сказала мне, когда ты искал Монику."
    show sayori 1b at t11 zorder 4
    "Нацуки? Это даёт мне возможность помочь ей."
    mc "Ладно, тогда я пойду поговорю с ней."
    show sayori 1a at t11 zorder 4
    mc "Я скоро вернусь!"
    show sayori 2r at f11 zorder 4
    s "Хорошо!"
    scene bg club_day with wipeleft_scene
    "Я иду к Нацуки."
    mc "Эй, Нацуки!"
    show natsuki 1k at t11 zorder 4
    "Она смотрит на меня с растерянным выражением лица."
    show natsuki 2b at f11 zorder 4
    n "Разве ты и [persistent.sayoriname] не хотели провести время вместе?"
    show natsuki 2za at t11 zorder 4
    mc "[persistent.sayoriname] сказала мне, что ты хотела поговорить со мной о чём-то."
    show natsuki 5d at f11 zorder 4
    n "О, я чуть не забыла."
    n 5m "Ты, наверно, заметил, что Юри здесь нет."
    n "Я не знаю куда она ушла, но она сказала что сейчас вернётся."
    n "Но прошло слишком много времени, я начинаю беспокоиться о ней."
    show natsuki 5n at t11 zorder 4
    "..."
    stop music fadeout 3.5
    window hide
    pause(4.0)
    "Уже началось, замечательно..."
    "Я думаю, это время решить всё по-настоящему."
    mc "Не волнуйся, я пойду искать её, я знаю, о чём идёт речь."
    show natsuki 1k at f11 zorder 4
    n "Ты знаешь?.."
    show natsuki at thide zorder 4
    hide natsuki
    "Не раздумывая, я выбегаю из комнаты."
    scene bg corridor with wipeleft_scene
    "Нельзя терять ни минуты, нужно сконцентрироваться..."
    play sound Glow
    window hide
    pause(3.0)
    "Она рядом!"
    scene bg black with dissolve
    "Я оказываюсь перед классной комнатой."
    "Так вот куда она уходит всё время?"
    "Неважно..."
    "Я открываю дверь."
    scene bg class_day
    show yuri 3p at f11 zorder 4
    y "Ах-х-х!!"
    y 1q "[player], что ты здесь делаешь?"
    show yuri at t11 zorder 4
    mc "..."
    mc "Прекрати притворяться, Юри."
    show yuri 1n at f11 zorder 4
    y "Притворяться? {w=0.6}{nw}"
    extend 1q "О ч-чём... ты говоришь?"
    show yuri at t11 zorder 4
    menu:
        "..."
        "Раскрыть её секрет":
            $ value = 11
        "Спокойно рассказать ей":
            $ value = 12
    if value == 11:
        mc "{w=0.5}.{w=0.5}.{w=0.5}."
        show yuri 3n at h11 zorder 4
        "Я с силой хватаю её за руку."
        "Она уже пытается вырваться, но тщетно, несмотря на то, как мало сил я приложил."
        show yuri 3p at f11 zorder 4
        y "[player]?! Ч-что ты делаешь...?!"
        show yuri 1pcuts at t11 zorder 4
        "Я закатываю ее рукав, теперь все её порезы видны нам обоим."
        y "..."
        window hide
        pause(2.0)
        mc "Ты делала это с собой всё это время..."
        show yuri at f11 zorder 4
        y "Н-нет!"
        show yuri 4b at t11 zorder 4
        "Она быстро прячет свои порезы обратно под рукав."
        show yuri 4f at t11 zorder 4
        window hide
        pause(2.0)
        jump phase5

    if value == 12:
        mc "{w=0.5}.{w=0.5}.{w=0.5}."
        mc "Я знаю, что ты делаешь с собой, Юри."
        show yuri 1n at t11 zorder 4
        "Она больше не сможет скрывать это."
        show yuri at f11 zorder 4
        y "..."
        y "Т-ты знаешь?"
        show yuri at t11 zorder 4
        mc "Я знаю всё, поэтому, пожалуйста... не усугубляй."
        show yuri 1t at t11 zorder 4
        window hide
        pause(2.0)
        show yuri 2w at t11 zorder 4
        "С разочарованным выражением на лице она начинает закатывать рукав."
        show yuri 1vcuts at t11 zorder 4
        window hide
        pause(3.0)
        mc "Ты делала это с собой всё это время, не так ли?"
        show yuri 4b at t11 zorder 4
        "Она прячет порезы сразу после того, как я спросил."
        show yuri 4f at t11 zorder 4
        window hide
        pause(2.0)
        jump phase5

label phase5:
    play music mend
    mc "Юри... почему ты не сказала об этом раньше?"
    show yuri 2z at f11 zorder 4
    y "Я... "
    extend 2x "Я не хотела беспокоить тебя этим."
    show yuri 3zh at f11 zorder 4
    y "Тебе было весело разговаривать со всеми, и если бы я сказала тебе, то ты бы только больше беспокоился обо мне."
    y 3z "Я не хочу, чтобы ты беспокоился обо мне, ты не сможешь помочь..."
    show yuri at t11 zorder 4
    mc "..."
    mc "Вот тут ты ошибаешься."
    mc "Скрывая это от нас, ты не сделаешь лучше."
    show yuri 3zh at t11 zorder 4
    mc "Должно быть, это оказывало на тебя слишком большое давление!"
    show yuri 3z at t11 zorder 4
    window hide
    pause(3.0)
    show yuri 3x at f11 zorder 4
    y "Ты не должен был этого видеть,{w=0.7} теперь ты, наверное, думаешь, что я уро-{nw}"
    show yuri at t11 zorder 4
    mc "Нет."
    mc "Ты не странная, ты не уродка, никто из нас не думает о тебе так."
    mc "Потому что ты наш друг, и мы просто хотим, чтобы ты чувствовала себя лучше."
    show yuri 2zh at f11 zorder 4
    y "..."
    y 2z "Я пыталась остановить это... ради вас."
    y 2zf "Но я не смогла... Я так слаба! Я больше не могу это остановить!"
    show yuri 2y at t11 zorder 4
    mc "Юри..."
    window hide
    pause(1.5)
    scene bg black with dissolve_scene_full
    "Я подхожу к ней и обнимаю её."
    mc "Возможно, ты не сможешь остановить это самостоятельно."
    mc "Но у тебя есть я, у тебя есть мы, помнишь?"
    y "..."
    y "Я не могу сказать Нацуки, она перестала бы разговаривать со мной..."
    mc "Ты правда в это веришь? Нацуки сказала мне об этом в первую очередь."
    mc "Она ужасно беспокоится о тебе, больше, чем кто-либо другой."
    y "Она...{w=1} это правда?"
    y "{w=0.5}.{w=0.5}.{w=0.5}."
    y "Я просто усложняю ей всё, не так ли...?"
    mc "Я уверен, что она смогла бы помочь, если бы знала об этом."
    mc "Знаешь... Я не заставляю тебя рассказывать остальным, я понимаю, что тебе нужно время."
    mc "Но пожалуйста... не игнорируй это, это важно для тебя."
    y "..."
    y "Я...{w=0.7} я попытаюсь."
    y "[player]."
    mc "М-м-м?"
    y "Спасибо..."
    y "Большое спасибо...{w=0.6} Мне действительно это было нужно."
    mc "В любое время, Юри."
    window hide
    pause(1.0)
    scene bg class_day with dissolve_scene_full
    show yuri 3ze at t11 zorder 4
    pause(2.0)
    show yuri 3u at t11 zorder 4
    "Она вытирает слёзы."
    mc "Чувствуешь ли ты себя лучше теперь, когда ты этого не скрываешь?"
    show yuri 3zi at f11 zorder 4
    y "Немного лучше..."
    y 2w "Но... "
    extend 2v "Просто мне кажется неправильным сваливать всё это на тебя."
    y 2t "Сейчас ты должен быть с [persistent.sayoriname]..."
    y "Вместо того, чтобы разговаривать со мной о моих проблемах."
    show yuri 2zg at t11 zorder 4
    mc "Я не хочу видеть, как ты делаешь это с собой, и я более чем уверен, что [persistent.sayoriname] чувствует то же самое."
    mc "И я не уйду, пока не помогу тебе..."
    show yuri 2w at f11 zorder 4
    y "..."
    y 2v "Тебе не следовало этого видеть..."
    y 3y "Мне правда жаль, [player]."
    show yuri at thide zorder 4
    hide yuri
    "Юри выбегает из класса."
    "{i}Х-х-х...{/i}"
    "Бедная Юри, она даже не знает, как к этому относиться..."
    scene bg corridor with dissolve
    "На безумной скорости я покидаю класс и замечаю Юри."
    "Она недостаточно быстра, чтобы убежать."
    scene bg black with dissolve
    pause(0.5)
    scene bg corridor with dissolve
    pause(1.0)
    show yuri 3zf at t11 zorder 4
    pause(1.0)
    show yuri at f11 zorder 4
    y "Ч-что?!"
    y "Н-но... ты б-был{w=0.3}{nw}"
    show yuri at t11 zorder 4
    mc "Успокойся, Юри..."
    show yuri 3y at t11 zorder 4
    window hide
    pause(2.5)
    mc "Я просто хочу, чтобы ты сказала мне..."
    mc "Ты тоже важна для меня, я не хочу видеть тебя такой."
    show yuri 2x at f11 zorder 4
    y "[player], я больше не могу вернуться..."
    y "Порезать себя – это единственное, что может избавить меня от этих сильных чувств."
    show yuri at t11 zorder 4
    mc "Это совсем не так."
    show yuri 2zh at t11 zorder 4
    mc "Я знаю, что это будет трудно для тебя."
    mc "Но ты должна понять, резать себя – это неправильный способ..."
    show yuri 2z at f11 zorder 4
    y "{w=0.5}.{w=0.5}.{w=0.5}."
    y 2x "[player], как ты вообще хочешь мне помочь?"
    show yuri at t11 zorder 4
    mc "..."
    mc "Есть несколько людей, которые переживают то же, что и ты."
    show yuri 2zh at t11 zorder 4
    mc "Они проходили через это долгое время, никогда не открываясь другим."
    mc "Это чуть не закончилось тем, что они покончили с собой..."
    show yuri 3y at t11 zorder 4
    window hide
    pause(2.0)
    mc "Но я пришёл и помог им, пообещав, что буду рядом с ними, когда им это понадобится."
    mc "И это именно то, что я собираюсь сделать для тебя, Юри."
    mc "Я забочусь обо всех вас, и я не хочу видеть, как кто-то из вас чувствует себя подавленным..."
    mc "Я знаю, сколько ужасных вещей может случиться с тобой."
    mc "И я хочу сделать всё, чтобы предотвратить это."
    show yuri 3zh at f11 zorder 4
    y "[player]..."
    show yuri 3z at t11 zorder 4
    window hide
    pause(3.0)
    show yuri 2x at f11 zorder 4
    y "Не трать время на меня, я этого не заслуживаю."
    y 2zh "Я не заслуживаю никого из вас..."
    y 2x "Ты не сможешь переубедить меня..."
    show yuri at t11 zorder 4
    mc "..."
    window hide
    pause(3.0)
    mc "Это то же самое, что они сказали мне тогда."
    show yuri 2zh at t11 zorder 4
    mc "Несмотря на это, я отказывался в это верить, и я знаю, что ты тоже можешь измениться."
    mc "Так что, пожалуйста... если ты не хочешь делать это для себя, тогда сделай для меня."
    mc "Сделай для Нацуки, [persistent.sayoriname], Моники..."
    show yuri 3zh at t11 zorder 4
    "Она молчит, её взгляд говорит, что прямо сейчас она борется со своими чувствами."
    "В ней тоже есть сила, я уверен в этом."
    show yuri at thide zorder 4
    hide yuri
    "Она бросается ко мне и обнимает меня, дрожа и громко плача."
    "Для неё это сложнее, чем я думал..."
    y "Мне так жаль!"
    mc "Тебе не должно быть, по крайней мере, ты готова попробовать."
    mc "Это всё, что имеет значение, я помогу тебе пройти через это, хорошо?"
    mc "Всегда помни, мы здесь, чтобы поддержать тебя..."
    y "..."
    y "Я не хочу потерять тебя..."
    y "Вот почему я скрывала это, я боюсь испортить отношения между нами."
    y "Я просто не хочу разрушать наш клуб..."
    mc "{w=0.5}.{w=0.5}.{w=0.5}."
    window hide
    pause(3.0)
    mc "Мы можем предотвратить это, если будем вместе."
    mc "Я верю, что ты понимаешь."
    mc "Ты всегда была понимающим человеком, Юри."
    window hide
    pause(2.5)
    show yuri 2s at t11 zorder 4
    pause(2.0)
    show yuri 1t at f11 zorder 4
    y "[player], может, нам стоит вернуться?"
    y "Нацуки, должно быть, сейчас волнуется..."
    show yuri at t11 zorder 4
    mc "О, точно! Мы не должны заставлять её больше ждать."
    show yuri 2f at f11 zorder 4
    y "Подожди, перед тем, как мы пойдём..."
    y "Как тебе удалось так быстро догнать меня раньше?"
    show yuri 2e at t11 zorder 4
    mc "..."
    window hide
    pause(3.0)
    mc "Я не уверен, могу ли я сказать тебе это или нет, Юри..."
    "Она выглядит очень растерянной, задаваясь вопросом, что я только что сказал ей."
    show yuri 2f at f11 zorder 4
    y "[player], ты...{w=0.6} тоже что-то скрываешь?"
    show yuri 2e at t11 zorder 4
    mc "Это слишком сложно объяснить несколькими словами..."
    mc "Если хочешь, мы можем поговорить об этом после того, как уйдем."
    mc "Это будет долгий разговор..."
    show yuri 1b at f11 zorder 4
    y "До тех пор, пока тебя это устраивает."
    y 1q "Вы с [persistent.sayoriname] в последнее время проводите много времени вместе, я не хочу прерывать вас..."
    show yuri 1u at t11 zorder 4
    mc "Все в порядке, теперь мы живём вместе, я скажу ей, что мне нужно обсудить с тобой важную тему."
    show yuri 2f at f11 zorder 4
    y "Вы живёте вместе?"
    y "Я думала, вы просто соседи."
    show yuri 2e at t11 zorder 4
    mc "Мы были соседями раньше, пока я не съехал."
    mc "У меня была причина сделать это, но я не могу озвучить её, прости..."
    show yuri 1d at f11 zorder 4
    y "Всё в порядке, ты не обязан говорить мне."
    show yuri 1o at f11 zorder 4
    y  "Но что я скажу Нацуки? Я не готова рассказать ей об этом..."
    show yuri at t11 zorder 4
    mc "Оставь это мне, я знаю, что сказать ей."
    mc "Пошли, если ты готова."
    show yuri 1q at f11 zorder 4
    y "Я...{w=0.5} я думаю, я готова."
    show yuri at t11 zorder 4
    "Я просто надеюсь, что она справится с этим..."
    "Будет лучше, если она расскажет Нацуки, но подталкивать её к этому неправильно."
    mc "Отлично, тогда идём!"
    stop music fadeout 2.0
    scene bg club_day with wipeleft_scene
    "Когда мы возвращаемся в клубную комнату, Нацуки идёт прямо к нам."
    play music t5
    show natsuki 4l at f11 zorder 4
    n "Вот вы где, я думала, вы двое больше не вернётесь."
    n 5k "Что случилось?"
    show natsuki at t22 zorder 3
    show yuri 4b at t21 zorder 4
    "Юри отводит взгляд, полностью полагаясь на то, что я собираюсь сказать."
    mc "Эм...{w=0.6} ну..."
    mc "Юри чувствовала себя немного подавленной, поэтому я пошёл и подбодрил её."
    show yuri 2s at t21 zorder 4
    show natsuki 2j at t22 zorder 3
    "Я не был уверен, что это было лучшее, что я мог сказать."
    "Юри, кажется, довольна этим ответом."
    "Я не хочу лгать Нацуки, но в то же время я не могу заставить себя рассказать ей о том, через что проходит Юри."
    show natsuki 2d at f22 zorder 4
    n "Так вот в чем дело."
    n 2m "Юри, ты могла бы сказать мне."
    show natsuki at t22 zorder 3
    show yuri 4b at f21 zorder 4
    y "П-прости, Нацуки."
    y 2v "Я просто не хотела беспокоить тебя по этому поводу."
    y "Это не серьёзно..."
    show yuri at t21 zorder 3
    show natsuki at f22 zorder 4
    n "Это серьёзно! Ты не сможешь наслаждаться чтением, если чувствуешь себя подавленной."
    n 5y "И самое главное, моими кексами!"
    show yuri 3c at t21 zorder 3
    show natsuki at t22 zorder 4
    "Юри слегка смеётся, как будто она внезапно забыла обо всём."
    "Это впечатляющая работа от Нацуки..." 
    mc "Я вернусь к [persistent.sayoriname], веселитесь!"
    show yuri 1a at t21 zorder 3
    show natsuki 5t at f22 zorder 4
    n "Я думаю, что я у тебя в долгу, [player]."
    show natsuki at t22 zorder 4
    mc "Ты мне ничем не обязана, в конце концов, это было важно для нас обоих."
    show natsuki 2z at f22 zorder 4
    n "Раз уж ты так говоришь, увидимся позже!"
    show natsuki at t22 zorder 3
    show yuri 1b at f21 zorder 4
    y "Увидимся позже, [player]."
    scene bg club_day with wipeleft_scene
    "[persistent.sayoriname] ждала довольно долго..."
    show sayori 2x at f11 zorder 4
    s "[player], ты вернулся!"
    show sayori 1a at t11 zorder 4
    mc "Да, это оказалось довольно важно."
    mc "Кроме того, мне нужно поговорить с Юри после того, как мы уйдем."
    mc "Ты не против побыть немного одной?"
    show sayori 2r at f11 zorder 4
    s "Конечно! Не волнуйся обо мне!"
    s 1l "Просто возвращайся поскорее, я буду очень скучать по тебе."
    show sayori 1y at t11 zorder 4
    mc "Я тоже буду скучать, но я вернусь раньше, чем ты успеешь оглянуться!"
    show sayori 1d at t11 zorder 4
    mc "Мы можем поиграть после того, как я вернусь."
    show sayori 4s at f11 zorder 4
    s "Я бы с удовольствием!"
    s 2c "Кстати, что произошло до этого? Ты выбежал из комнаты очень быстро."
    show sayori 2b at t11 zorder 4
    mc "..."
    mc "Юри чувствовала себя подавленной, я это чувствовал, поэтому я выбежал, чтобы помочь ей."
    show sayori 2h at f11 zorder 4
    s "Она в порядке?"
    show sayori 2g at t11 zorder 4
    mc "Да, сейчас ей лучше."
    show sayori 1d at t11 zorder 4
    "Мне правда жаль, [persistent.sayoriname], но я не делаю исключений..."
    mc "Это одна из причин, по которой я поговорю с ней, я хочу немного подбодрить её."
    show sayori 2d at t11 zorder 4
    window hide
    pause(2.0)
    show sayori 2r at f11 zorder 4
    s "Если ты помогаешь ей, то она в мгновение ока забудет обо всём, что её беспокоит!"
    show sayori 1a at t11 zorder 4
    mc "Исходя из собственного опыта, не так ли?"
    show sayori 1y at f11 zorder 4
    s "..."
    show sayori at t11 zorder 4
    window hide
    stop music fadeout 2.5
    pause(3.0)
    play music t9
    show sayori 2zc at f11 zorder 4
    s "Я чувствую себя лучше благодаря тебе, [player]."
    s "И я не забуду, через что ты прошёл, просто чтобы помочь такой глупой девочке, как я."
    show sayori 2d at t11 zorder 4
    mc "Ты не глупая, это не твоя вина, что у тебя такая проблема."
    mc "У меня было нечто подобное в прошлом, и я не хочу, чтобы ты испытала что-то ещё хуже, чем это..."
    show sayori 1h at f11 zorder 4
    s "У тебя тоже была депрессия?"
    show sayori 1g at t11 zorder 4
    mc "Это было не так плохо, как в твоём случае, но я просто хотел уйти и быть всеми забытым."
    mc "В моём сердце не было ничего, кроме ненависти."
    mc "Но не волнуйся, я больше не чувствую это."
    show sayori 1d at t11 zorder 4
    window hide
    pause(2.0)
    show sayori 2h at f11 zorder 4
    s "[player], если ты когда-нибудь снова начнёшь чувствовать то же самое, я тоже буду здесь ради тебя."
    s "Не забывай о себе, я тоже забочусь о тебе."
    s "Твоё счастье – самое важное для меня..."
    show sayori 2g at t11 zorder 4
    mc "Я не позволю этому случиться со мной дважды, я позабочусь об этом."
    show sayori 2d at t11 zorder 4
    window hide
    pause(2.0)
    show sayori 4s at f11 zorder 4
    s "Хорошо, но это не значит, что я перестану присматривать за тобой!"
    show sayori 4q at t11 zorder 4
    mc "Хе-хе, я и не ожидаю этого."
    show sayori 1a at t11 zorder 4
    mc "Но мне уже достаточно просто быть с тобой."
    show sayori 1d at t11 zorder 4
    window hide
    pause(2.0)
    show sayori 2d at t11 zorder 4
    "Она хватает меня за руку."
    show sayori 2s at f11 zorder 4
    s "Тогда я никуда не отпущу тебя без меня сегодня, хе-хе."
    s 5a "Просто шутка, я бы никогда не заставила тебя быть со мной."
    s 1c "Но я хотела спросить тебя кое о чём."
    s "Это нормально, если ты не хочешь говорить мне, но о чём вы с Юри будете говорить?"
    show sayori 1b at t11 zorder 4
    mc "Ну{w=0.5}.{w=0.5}.{w=0.5}."
    window hide
    stop music fadeout 3.0
    pause(3.5)
    mc "Она видела то, чего не должна была видеть..."
    mc "И я хочу объяснить это ей."
    show sayori 2h at f11 zorder 4
    s "Это насчёт твоих..."
    show sayori 2g at t11 zorder 4
    mc "Сил, которым не место в этом мире? Да..."
    mc "Не волнуйся, я знаю, что ей сказать, она поймёт."
    show sayori 1h at f11 zorder 4
    s "Я могу помочь!"
    show sayori 1g at t11 zorder 4
    mc "Нет, всё в порядке. Я справлюсь."
    mc "Кроме того... как бы ты объяснила ей, что знаешь об этом?"
    show sayori 1k at f11 zorder 4
    s "Оу..."
    play music t2
    s 2l "Хе-хе... На самом деле, я не думала об этом."
    show sayori at t11 zorder 4
    mc "Я привык решать проблемы самостоятельно, так что тебе не нужно беспокоиться об этом."
    show sayori 1x at f11 zorder 4
    s "Хорошо, но напиши мне, если я тебе понадоблюсь."
    show sayori 1a at t11 zorder 4
    mc "Хорошо!"
    scene bg black with dissolve_scene_full
    "Время проходит, и мы собираемся уходить."
    "Моника выходит первой, выражение её лица не меняется, она по-прежнему выглядит такой же подавленной, как и раньше."
    scene bg club_day with dissolve_scene_full
    pause(1.0)
    show sayori 2c at f11 zorder 4
    s "[player], ты собираешься уйти с Юри, верно?"
    show sayori 2b at t11 zorder 4
    mc "Да."
    show sayori 1l at f11 zorder 4
    s "Тогда я пойду."
    s 1zc "Скоро увидимся!"
    show sayori 1d at t11 zorder 4
    mc "Увидимся позже, [persistent.sayoriname]."
    show sayori at thide zorder 4
    hide sayori
    "Мы обнимаем друг друга, прежде чем она уходит."
    "Кажется, что Нацуки тоже собирается уходить, и Юри начинает приближаться ко мне."
    show yuri 1b at f11 zorder 4
    y "[player], куда нам следует пойти?"
    show yuri 1a at t11 zorder 4
    mc "Мы могли бы пойти ко мне домой, у меня всё ещё есть ключи."
    mc "К тому же, там нас никто не сможет прервать."
    show yuri 2d at f11 zorder 4
    y "Замечательно!"
    scene bg black with dissolve_scene_full
    "Мы подходим к моему дому и входим в него."
    scene bg kitchen with dissolve_scene_full
    pause(1.0)
    show yuri 1b at f11 zorder 4
    y "Так вот как выглядит твой дом, довольно симпатично."
    y 1f "Жаль, что им сейчас не пользуются."
    show yuri 1e at t11 zorder 4
    mc "Не волнуйся, я знаю кое-кого, кому он нужен, я скоро отдам дом ей."
    mc "В любом случае, мы можем подняться наверх, в мою комнату."
    show yuri 1b at f11 zorder 4
    y "Конечно!"
    scene bg bedroom with dissolve_scene_full
    stop music fadeout 2.5
    pause(3.0)
    play music still
    show yuri 1a at t11 zorder 4
    mc "Что же{w=0.5}.{w=0.5}.{w=0.5}. с чего мне начать?"
    show yuri 2h at f11 zorder 4
    y "Я хотела знать..."
    y 2f "Когда я выбежала из той комнаты, я была уверена, что ты не сможешь меня догнать."
    y "Но потом я обнаружила, что ты стоишь прямо передо мной, как ты это сделал?"
    show yuri 2e at t11 zorder 4
    mc "Ты можешь не поверить в то, что сейчас услышишь."
    show yuri 1b at f11 zorder 4
    y "Ну же, дай мне шанс."
    show yuri 1a at t11 zorder 4
    mc "{w=0.5}.{w=0.5}.{w=0.5}."
    window hide
    pause(2.0)
    mc "Я обладаю силами, о которых этот мир не знает."
    show yuri 1e at t11 zorder 4
    mc "Вот как я смог добраться туда так быстро."
    window hide
    pause(2.0)
    show yuri 3d at t11 zorder 4
    "Она начинает смеяться, как я и ожидал."
    show yuri 1b at f11 zorder 4
    y "Я знал, что ты собирался оправдываться передо мной, но это забавно, [player]."
    show yuri 1a at t11 zorder 4
    mc "..."
    show yuri 3p at h11 zorder 4
    play sound "sfx/fire2.ogg"
    "Я создаю огонь в своих руках, немедленно убеждая её."
    mc "Ты действительно думаешь, что я пошутил?"
    mc "Это не оправдание, я серьёзно отношусь к тому, что сказал."
    show yuri 3n at f11 zorder 4
    y "Т-ты...?!"
    y "К-как{w=0.2}{nw}"
    show yuri at t11 zorder 4
    mc "Успокойся, пожалуйста..."
    window hide
    pause(2.5)
    "Она немного отступает."
    window hide
    pause(1.5)
    "Возможно, это было немного чересчур, чтобы показывать ей."
    mc "Извини, я не хотел тебя пугать, но иначе ты бы не поверила."
    show yuri at f11 zorder 4
    y "{w=0.5}.{w=0.5}.{w=0.5}."
    y "К-как ты можешь это делать?!"
    show yuri at t11 zorder 4
    mc "Прежде чем я начну объяснять, тебе следует потратить минутку, чтобы успокоиться."
    show yuri 2o at t11 zorder 4
    window hide
    pause(2.5)
    show yuri 2w at t11 zorder 4
    "Она делает глубокий вдох, но я не удивлён, почему она так реагирует."
    "Кто бы так не реагировал после того, как увидел то, что, по их мнению, нереально?"
    window hide
    pause(1.5)
    show yuri 2t at f11 zorder 4
    y "Поэтому твои глаза меняют цвет?"
    y "И вот как ты узнал о моей проблеме?"
    show yuri at t11 zorder 4
    mc "..."
    mc "Да."
    mc "Я видел, как ты делала это с собой раньше, так что я знал это ещё до того, как вступил в Литературный клуб."
    mc "Это было неправильно, ты этого не заслуживаешь."
    mc "Вот почему я покинул свой мир, чтобы войти в ваш."
    mc "Я сделал это, чтобы всё исправить, видеть тебя в таком состоянии для меня неприемлемо."
    mc "И это даже не половина, если бы я мог рассказать тебе все причины..."
    show yuri 3t at f11 zorder 4
    y "[player]..."
    y "Ты сделал всё это, чтобы сделать клуб лучшим местом для меня?"
    show yuri at t11 zorder 4
    mc "Конечно, я не мог этого вынести, мне просто пришлось это изменить..."
    show yuri 2s at f11 zorder 4
    y "..."
    y 2zi "Спасибо, [player], это заставляет меня ценить то, что ты делаешь."
    y 2t "Но{w=0.5}.{w=0.5}.{w=0.5}. ты правда уверен в этом?"
    y "А что насчёт твоих друзей? Семьи?"
    show yuri at t11 zorder 4
    mc "Они понимают моё решение."
    mc "И они не смогли бы остановить меня, даже если бы захотели."
    mc "Я был уверен в этом выборе, поверь мне..."
    show yuri at f11 zorder 4
    y "..."
    y "Я не знаю, что сказать... но в то же время, у меня так много вопросов..."
    show yuri at t11 zorder 4
    mc "Не стесняйся спросить меня о чём-угодно."
    mc "Я не могу гарантировать, что отвечу на все вопросы, но я расскажу тебе всё, что смогу."
    show yuri 1v at t11 zorder 4
    "Честно говоря, с ней всё проще, чем я думал."
    "Особенно когда она не знакома с подобными способностями, живя в мире, где это считается просто фантастикой."
    show yuri 1t at f11 zorder 4
    y "Ты сказал, что видел, как я делала это с собой."
    y "Это было какое-то видение?"
    show yuri at t11 zorder 4
    mc "Нет, это было не видение."
    mc "В моём мире ваш мир воспринимается как видеоигра."
    mc "Многие люди там верят, что тебя даже не существует."
    show yuri 1n at f11 zorder 4
    y "Видеоигра?!"
    y 1o "..."
    show yuri at t11 zorder 4
    mc "Сначала всё было хорошо, но потом, внезапно, всё стало меняться к худшему."
    show yuri 2t at t11 zorder 4
    mc "Как итог{w=0.5}.{w=0.5}.{w=0.5}."
    window hide
    pause(2.0)
    mc "Я не думаю, что мне следует говорить тебе это."
    mc "Что ещё более важно, я не позволю этому случиться, я обещаю тебе."
    show yuri 2s at t11 zorder 4
    window hide
    pause(2.0)
    show yuri 1q at f11 zorder 4
    y "Следующий вопрос, который беспокоит меня больше всего..."
    y 1h "[persistent.sayoriname] всегда говорила о своём друге, которого она знает с детства."
    y 1f "Когда она представляла тебя нам, она сказала, что ты тот самый друг."
    y "Но если ты из другого мира, тогда как ты можешь быть её другом детства?"
    show yuri 1e at t11 zorder 4
    mc "Это хороший вопрос."
    mc "Этот её друг{w=0.5}.{w=0.5}.{w=0.5}. когда я вошёл в этот мир, мне показалось, что я заменил его собой."
    mc "Сейчас это звучит действительно странно, но это то, что, должно быть, произошло."
    mc "Возможно, он ненастоящий, или, может быть, это что-то, что мне ещё предстоит выяснить."
    mc "И [persistent.sayoriname], кажется, по какой-то причине помнит меня как этого друга..."
    show yuri 2v at f11 zorder 4
    y "Это звучит действительно безумно..."
    show yuri at t11 zorder 4
    mc "Да, я знаю."
    show yuri 1w at t11 zorder 4
    window hide
    pause(2.0)
    show yuri 1t at f11 zorder 4
    y "Извини, если задаю слишком много вопросов."
    y 1v "Но есть ещё одна последняя вещь, которую я хотела бы знать..."
    y 2t "Ты, случайно не{w=0.5}.{w=0.5}.{w=0.5}. любишь [persistent.sayoriname]?"
    show yuri at t11 zorder 4
    mc "..."
    "Я должен был предвидеть, что это произойдёт."
    window hide
    pause(2.0)
    mc "Да, я люблю [persistent.sayoriname]."
    show yuri 1q at f11 zorder 4
    y "Оу..."
    y "Ладно, спасибо тебе за честность."
    show yuri 1u at t11 zorder 4
    mc "Юри... ты же не собираешься ревновать, правда?"
    show yuri 2n at f11 zorder 4
    y "Ч-что?!"
    y 2o "Нет!"
    y 1q "Я уважаю твоё решение."
    show yuri 1u at t11 zorder 4
    mc "{w=0.5}.{w=0.5}.{w=0.5}."
    mc "Я просто хочу убедиться, потому что это стало проблемой для тебя раньше."
    show yuri 2t at f11 zorder 4
    y "Что ты имеешь в виду?"
    show yuri at t11 zorder 4
    mc "Помимо твоих порезов, одержимость стала проблемой и для тебя..."
    mc "Могу сказать, это было очень неприятно."
    mc "Поэтому я хочу, чтобы ты избегала этого, пока ещё можешь."
    show yuri 1v at f11 zorder 4
    y "{w=0.5}.{w=0.5}.{w=0.5}."
    y 1t "Меня пугает, как много ты знаешь..."
    show yuri at t11 zorder 4
    mc "Это наименее пугающая вещь во мне."
    show yuri 2n at t11 zorder 4
    window hide
    pause(2.0)
    mc "Оу...{w=0.5} прости, я не хотел, чтобы это прозвучало так плохо."
    show yuri 2q at f11 zorder 4
    y "Нет, нет, всё в порядке..."
    y 2v "Всё это просто слишком много для меня."
    show yuri at t11 zorder 4
    mc "Я понимаю, не торопись."
    mc "Я не собираюсь давить на тебя."
    show yuri 1w at t11 zorder 4
    window hide
    pause(2.5)
    show yuri 1zi at f11 zorder 4
    y "Спасибо тебе."
    y 2f "У тебя здесь есть что-нибудь выпить? Я вроде как хочу пить."
    show yuri 2e at t11 zorder 4
    mc "Там всё ещё должно быть что-то, я не уверен..."
    mc "Это мой дом, но в то же время, это не так."
    show yuri 1q at f11 zorder 4
    y "Оу, верно..."
    y "Тогда я посмотрю внизу."
    show yuri at thide zorder 4
    hide yuri
    window hide
    pause(2.0)
    "Думаю, я мог бы немного вздремнуть, прежде чем она вернётся."
    stop music fadeout 3.0
    window hide
    pause(1.5)
    scene bg black with dissolve_scene_full
    pause(0.5)
    scene bg bedroom with dissolve_scene_full
    pause(1.5)
    "Как долго я спал?"
    "Юри ещё не вернулась, может, мне стоит пойти проведать её."
    scene bg kitchen with wipeleft_scene
    "Я хорошенько осматриваюсь."
    "{w=0.5}.{w=0.5}.{w=0.5}."
    "Её здесь тоже нет?"
    "Куда она делась..."
    window hide
    pause(2.0)
    "Она сбежала из-за того, что я ей сказал?"
    "..."
    "Нет, она бы этого не сделала, возможно, для этого есть другая причина."
    "Хорошо, я использую концентрацию внимания, чтобы выяснить."
    play sound Glow
    window hide
    pause(3.0)
    "Её нигде не найти, но..."
    "В доме [persistent.sayoriname] что-то изменилось, может быть, это как-то связано с этим?"
    "Что ж, есть только один способ выяснить это."
    scene bg house with wipeleft_scene
    "Но зачем ей идти в дом [persistent.sayoriname]?"
    "..."
    scene bg house_corridor with wipeleft_scene
    "Она действительно здесь?"
    "Ну... наверное, мне следует написать ей, или, может быть, [persistent.sayoriname] что-то знает."
    "Я постучал в дверь [persistent.sayoriname]."
    mc "[persistent.sayoriname]? Ты там?"
    mc "Мне нужно спросить тебя кое о чём важном."
    window hide
    pause(2.0)
    "Нет ответа."
    mc "[persistent.sayoriname]?"
    mc "..."
    "Моё внимание говорит мне, что здесь кто-то есть."
    "И это может быть только она, так почему же она не отвечает?"
    window hide
    pause(2.0)
    "Неважно."
    mc "Я вхожу, хорошо?"
    mc "Сайо-{nw}"
    window hide(None)
    window auto
    play music td
    show s_kill_bg2
    show s_kill2
    show s_kill_bg as s_kill_bg at s_kill_bg_start
    show s_kill as s_kill at s_kill_start
    $ pause(3.75)
    show s_kill_bg2 as s_kill_bg
    show s_kill2 as s_kill
    $ pause(0.01)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    hide s_kill_bg
    hide s_kill
    show s_kill_bg_zoom zorder 1
    show s_kill_bg2_zoom zorder 1
    show s_kill_zoom zorder 3
    show s_kill2_zoom zorder 3
    show s_kill as s_kill_zoom_trans zorder 3:
        truecenter
        alpha 0.5
        zoom 2.0 xalign 0.5 yalign 0.05
        pause 0.5
        dizzy(1, 1.0)
    $ pause(2.0)
    show noise zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.25
    show vignette zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.75
    $ pause(1.5)
    $ pause(1.5)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    pause(1.0)
    mc "Ч-ЧТО?!!"
    mc "ЧТО Я ВИЖУ?!!"
    mc "С-[persistent.sayoriname]?!{w=1} НЕТ, НЕТ, НЕТ!!"
    mc "[persistent.sayoriname] НИКОГДА БЫ ЭТОГО НЕ СДЕЛАЛА, ПЕРЕСТАНЬ ПОКАЗЫВАТЬ МНЕ ЭТО!!!"
    mc "ЭТО НЕ РЕАЛЬНО, ЭТО НЕ РЕАЛЬНО, {b}ЭТО НЕ РЕАЛЬНО!!!{/b}"
    mc "{b}Я НЕ ВЕРЮ В ЭТО, Я НЕ ХОЧУ ВИДЕТЬ ЭТО, ПРЕКРАТИ!!!{/b}"
    stop music
    show screen tear(25, 0.05, 0.05, -20, 80)
    play sound "sfx/glitch2.ogg"
    window hide
    pause(0.6)
    hide screen tear
    scene bg bedroom
    show yuri 3p at f11 zorder 4
    y "[player]?!!"
    y "Ч-что произошло?!"
    scene bg black with dissolve
    pause(1.0)
    "Я встаю с кровати и со скоростью звука покидаю дом, чтобы найти [persistent.sayoriname]."
    "В мгновение ока я оказываюсь в гостиной."
    scene bg living_room_late with dissolve_scene_full
    pause(0.5)
    mc "[persistent.sayoriname]!!"
    "Она слышит меня и приходит в гостиную."
    show sayori 2bc at f11 zorder 4
    s "[player]?"
    show sayori 2bb at t11 zorder 4
    "Почти мгновенно она замечает моё тяжёлое дыхание и отчаяние в моих глазах."
    show sayori 4bw at f11 zorder 4
    s "[player]?! Что происходит?!"
    show sayori at thide zorder 4
    hide sayori
    play music t9
    "Я обнимаю её, всё ещё дрожа после того, что я увидел."
    mc "Я так рад... т-так рад, что с тобой ничего не случилось."
    mc "З-зрелище... Я не мог{w=0.5}.{w=0.5}.{w=0.5}. Я просто не мог-{nw}"
    show sayori 2bzd at f11 zorder 4
    s "Тс-с-с... всё хорошо, [player]."
    s "Сейчас я с тобой, пожалуйста, успокойся..."
    show sayori 2bt at t11 zorder 4
    window hide
    pause(2.5)
    mc "Даже если я не верил в то, что видел..."
    mc "Всё казалось таким... реальным..."
    show sayori 1bv at f11 zorder 4
    s "Что ты видел?"
    show sayori at t11 zorder 4
    mc "Я..."
    mc "Я видел... к-как ты висела на потолке."
    show sayori 2bv at f11 zorder 4
    s "[player]... вот почему ты дрожишь?"
    s "Ты всё ещё беспокоишься?"
    show sayori at t11 zorder 4
    mc "Н-нет, я знаю, ты бы этого не сделала."
    mc "Но эта мысль всё ещё ужасает... я не хочу этого видеть, я не хочу, чтобы это когда-нибудь случилось!"
    show sayori 1bu at t11 zorder 4
    window hide
    pause(2.5)
    show sayori 2bzd at f11 zorder 4
    s "Ты можешь спать рядом со мной этой ночью, если хочешь."
    show sayori 2bt at t11 zorder 4
    mc "..."
    mc "Я{w=0.5}.{w=0.5}.{w=0.5}. я бы с удовольствием."
    show sayori 1bt at t11 zorder 4
    window hide
    pause(2.0)
    show sayori 4bs at f11 zorder 4
    s "У тебя не будет этих ужасных мыслей, когда ты будешь со мной!"
    show sayori at t11 zorder 4
    mc "Спасибо, [persistent.sayoriname]..."
    show sayori 2bd at t11 zorder 4
    mc "Ты даже не представляешь, как сильно мне это нужно."
    show sayori 1bb at t21 zorder 3
    show yuri 2n at f22 zorder 4
    y "[player]! Вот ты где!"
    show yuri at t22 zorder 3
    show sayori 1bc at f21 zorder 4
    s "Юри? Что ты здесь делаешь?"
    show sayori 1bb at t21 zorder 3
    show yuri 2v at f22 zorder 4
    y "[player] и я разговаривали, а потом я пошла купить чего-нибудь выпить."
    y 2t "Но когда я вернулась наверх, он кричал во сне."
    y "После этого он встал и убежал..."
    show sayori 1bg at t21 zorder 3
    y "Что беспокоит меня больше всего, так это то, что он выкрикивал твоё имя очень расстроенным голосом."
    show yuri 2zg at t22 zorder 3
    window hide
    pause(2.5)
    show sayori 2bh at f21 zorder 4
    s "[player], должна ли я рассказать ей всё?"
    show sayori 2bg at t21 zorder 4
    mc "..."
    show sayori 2bg at t21 zorder 4
    mc "Только если ты действительно в этом уверена."
    mc "Это полностью зависит от тебя..."
    show sayori 2bf at t21 zorder 4
    window hide
    pause (2.0)
    show sayori 1bk at f21 zorder 4
    s "Юри..."
    window hide
    pause(2.5)
    show sayori 1bh at f21 zorder 4
    s "[player] беспокоится обо мне из-за моей депрессии."
    show yuri 2n at f22 zorder 4
    show sayori 1bg at t21 zorder 3
    y "Т-Ты?! У тебя депрессия?!"
    y "К-как?!"
    show yuri at t22 zorder 3
    show sayori 1bh at f21 zorder 4
    s "Это действительно правда, Юри."
    s "[player] заметил это давным-давно, он пытается утешить меня."
    show yuri 3t at t22 zorder 4
    s 2bh "Он даже переехал из своего дома, чтобы подбодрить меня и заставить чувствовать себя лучше."
    s "И если бы не он,{w=0.7} тогда меня бы здесь даже не было..."
    show yuri 3t at f22 zorder 4
    show sayori 1bf at t21 zorder 3
    y "{w=0.5}.{w=0.5}.{w=0.5}."
    y "[persistent.sayoriname]... Я понятия не имела..."
    y 2v "Это многое объясняет..."
    y 2t "[player], это то, о чём ты хотел поговорить?"
    show yuri at t22 zorder 3
    mc "Да..."
    mc "Ты должна понять, я бы не стал подталкивать [persistent.sayoriname] к разговору об этом."
    show yuri 1zi at f22 zorder 4
    y "Я понимаю, {w=0.6}{nw}"
    extend 1f "но я хочу кое-что узнать у тебя, [persistent.sayoriname]."
    show yuri 1e at t22 zorder 3
    show sayori 2bc at f21 zorder 4
    s "Ась?"
    show sayori 2bb at t21 zorder 3
    show yuri 1f at f22 zorder 4
    y "Насколько хорошо ты знаешь {b}его{/b}?"
    show yuri 1e at t22 zorder 3
    show sayori 1bg at t21 zorder 4
    mc "Всё в порядке, ты можешь рассказать ей всё."
    mc "Мы зашли так далеко, я уже не вижу других вариантов."
    show sayori 1bk at f21 zorder 4
    s "..."
    s 1bh "Я знаю, Юри, ты можешь не бояться."
    s "Но [player] на самом деле не тот друг, которого я знаю, он{w=0.25}.{w=0.25}.{w=0.25}. из другого мира."
    s "Я знаю, это звучит так, будто я издеваюсь над тобой, но я говорю правду."
    show sayori 1bg at t21 zorder 3
    show yuri 2q at f22 zorder 4
    y "Не волнуйся, я уже видела, что он может сделать, я знаю, что ты не лжёшь."
    show yuri 2u at t22 zorder 3
    show sayori 2bc at f21 zorder 4
    s "Так ты всё знаешь?.."
    show sayori 2bb at t21 zorder 3
    show yuri 1q at f22 zorder 4
    y "Я почти уверена, что не знаю о нём ничего."
    y "Но я знаю, что у него есть какие-то{w=0.5}.{w=0.5}.{w=0.5}. божественные силы..."
    show yuri 1u at t22 zorder 3
    show sayori 1bzc at f21 zorder 4
    s "Выходит, теперь я не единственная, кто это знает."
    show sayori 1bd at t21 zorder 4
    mc "У меня только одна маленькая просьба."
    show sayori 1bb at t21 zorder 3
    show yuri 1с at t22 zorder 4
    mc "Не говори об этом никому, надеюсь, ты понимаешь, почему."
    show sayori 2bx at f21 zorder 4
    s "Конечно!"
    show sayori 4ba at t21 zorder 3
    show yuri 2t at f22 zorder 4
    y "Надеюсь, ты скоро поправишься, [persistent.sayoriname]."
    show yuri at t22 zorder 3
    show sayori 4bs at f21 zorder 4
    s "Не беспокойся, когда [player] со мной общается, это помогает мне чувствовать себя лучше с каждым днём!"
    show sayori 4bq at t21 zorder 4
    "Я невольно краснею, услышав это."
    mc "Я всегда чувствую облегчение, когда тебе становится лучше, [persistent.sayoriname]."
    show sayori 3bd at t21 zorder 4
    "Она тянется ко мне и берёт меня за руку."
    show yuri 1q at f22 zorder 4
    y "О, наверное, мне стоит оставить вас двоих наедине, верно?"
    show yuri 1u at t22 zorder 3
    mc "Эй, Юри, помни, мы все встретимся здесь завтра."
    show sayori 4br at f21 zorder 4
    s "Уверена, вам понравится!"
    s 2bx "Не забудь взять с собой чай, хорошо?"
    show sayori 4ba at t21 zorder 3
    show yuri 2d at f22 zorder 4
    y "Вы можете рассчитывать на меня! Увидимся завтра."
    show yuri at thide zorder 4
    hide yuri
    "Юри уходит, мол, она уже приняла ситуацию такой, какая она есть."
    window hide
    pause (2.0)
    "{i}Х-х-х…{/i}"
    show sayori at t11 zorder 4
    mc "Прости, [persistent.sayoriname]."
    show sayori 1bb at t11 zorder 4
    mc "Этого не должно было случиться, я не знаю, почему ты сразу согласилась сказать ей..."
    show sayori 1bg at t11 zorder 4
    mc "Просто... Я так волновался, что с тобой действительно что-то случилось."
    mc "И я бы не знал, что делать, если бы это действительно произошло."
    show sayori 2bzc at f11 zorder 4
    s "Нет, всё в порядке, [player]."
    s "Я бы всё равно сказала ей рано или поздно."
    s 1bzc "Она тоже заслуживает это знать, она наш друг."
    show sayori 1bd at t11 zorder 4
    mc "..."
    mc "Да, ты права."
    mc "В любом случае, сейчас я ничего не могу с этим поделать."
    mc "Мы хотели поиграть в игры, да?"
    show sayori 2bx at f11 zorder 4
    s "О, конечно! Я тоже принесу что-нибудь поесть."
    scene bg black with dissolve_scene_full
    "Мы тратим довольно много времени на то, чтобы облегчиться после того, что произошло."
    "Я полностью успокоился, а [persistent.sayoriname], скорее всего, перестала об этом думать."
    "Теперь, когда Юри и [persistent.sayoriname] знают, а также знают, что другая знает о моих способностях, мне может быть немного легче."
    window hide
    pause (1.0)
    scene bg living_room_late with dissolve_scene_full
    pause(0.5)
    show sayori 5bb at f11 zorder 4
    s "Вау, ты действительно хорош в этом."
    s 2bx "Как ты научился так хорошо играть?"
    show sayori 4ba at t11 zorder 4
    mc "Ха-ха, ну... Я играл в игры каждый день, прежде чем покинуть свой мир."
    mc "Мои друзья, наверное, скучают по тем дням, когда мы играли почти целыми днями."
    show sayori 1bh at f11 zorder 4
    s "Ты знаешь, что это вредно для здоровья, да?"
    show sayori 1bg at t11 zorder 4
    mc "Я знаю, я знаю..."
    mc "Но оно того стоило, это то, что я никогда не забуду."
    show sayori 1bd at t11 zorder 4
    window hide
    pause (2.0)
    show sayori 2bzc at f11 zorder 4
    s "Если тебе так нравится, то мы можем играть чаще."
    show sayori 2bd at t11 zorder 4
    mc "Ты действительно этого хочешь?"
    show sayori 4bs at f11 zorder 4
    s "Конечно хочу!"
    s 2bzc "Я не против, лишь бы тебе это нравилось."
    show sayori 2bd at t11 zorder 4
    mc "..."
    mc "[persistent.sayoriname], ты самый хороший человек, которого я когда-либо знал..."
    show sayori 1by at f11 zorder 4
    s "О-о-о... ты же знаешь, что это неправда."
    show sayori 3be at t11 zorder 4
    "Я осторожно беру её за руку."
    mc "Это правда."
    mc "Почти все меня боятся, и никогда бы не сделали ничего подобного, если бы я их не заставлял."
    mc "Я очень ценю тебя за то, кто ты есть, [persistent.sayoriname]."
    mc "Пожалуйста, никогда не забывай, кто ты для меня."
    window hide
    pause (2.0)
    show sayori 3bd at t11 zorder 4
    pause(1.5)
    show sayori 3bzc at f11 zorder 4
    s "Я не забуду, я люблю тебя, [player]."
    scene bg black with dissolve_scene_full
    stop music fadeout 2.0
    pause(2.5)
    "После тяжелого дня мы с [persistent.sayoriname] решили лечь спать."
    "Теперь я чувствую, что способен наилучшим образом защитить её."
    "Я крепко обнимаю её, ощущая её тепло всю ночь."
    window hide
    pause (2.0)
    scene bg sayori_bedroom with dissolve_scene_full
    "Прежде чем я это осознал, уже наступило утро."
    "Обычно я не просыпаюсь так рано, но [persistent.sayoriname] собирается приготовить завтрак."
    show sayori 4pza at t11 zorder 4
    "Она зевает, когда начинает просыпаться вместе со мной."
    show sayori 2px at f11 zorder 4
    play music t8
    s "Доброе утро, [player]."
    show sayori 2pa at t11 zorder 4
    mc "Доброе утро, я вижу, ты уже встала, чтобы приготовить завтрак."
    show sayori 2pr at f11 zorder 4
    s "Да, и даже не думай, что я позволю тебе пропустить завтрак!"
    show sayori 2pq at t11 zorder 4
    mc "Хе-хе... этого и следовало ожидать от тебя."
    scene bg living_room with dissolve_scene_full
    pause (1.0)
    show sayori 1ba at t11 zorder 4
    mc "Итак, {w=0.25}.{w=0.25}.{w=0.25}. [persistent.sayoriname], когда мы встречаемся?"
    show sayori 5bb at f11 zorder 4
    s "Хе-хе-хе..."
    s 5ba "Я как бы... не подумала об этом."
    show sayori at t11 zorder 4
    mc "{i}Х-х-х…{/i}"
    show sayori 2bx at f11 zorder 4
    s "Всё в порядке, я сказала им, что я им напишу."
    show sayori 4ba at t11 zorder 4
    mc "Я могу это сделать, но как насчёт еды?"
    show sayori 4bm at f11 zorder 4
    s "О! Я должна купить её!"
    s 1bx "Это не займёт у меня много времени, я скоро буду!"
    show sayori 1ba at t11 zorder 4
    mc "Будь осторожна!"
    show sayori 3bq at f11 zorder 4
    "Она целует меня в щёку, прежде чем уйти."
    show sayori at thide zorder 4
    hide sayori
    window hide
    pause (2.0)
    "Я должен тем временем пойти проведать Монику, просто чтобы убедиться, что с ней всё в порядке."
    "И что она не собирается ничего предпринимать."
    scene bg black with wipeleft_scene
    stop music fadeout 3.0
    pause (1.0)
    scene bg house2 with wipeleft_scene
    pause(1.2)
    "Я звоню ей в дверь."
    window hide
    pause (2.0)
    "Ей нужно время, прежде чем она откроет."
    show monika 1bc at t11 zorder 4
    window hide
    pause(1.5)
    mc "Привет, Моника, у тебя всё хорошо?"
    show monika 2bo at f11 zorder 4
    m "..."
    play music t10
    m 2bp "Нет, у меня не всё хорошо."
    show monika 2bo at t11 zorder 4
    mc "Я должен был этого ожидать..."
    mc "Мы тебя сегодня приободрим, не волнуйся!"
    show monika 1bq at t11 zorder 4
    window hide
    pause (2.0)
    show monika 1bp at f11 zorder 4
    m "Я не думаю, что я должна здесь появляться."
    show monika 1bo at t11 zorder 4
    mc "..."
    mc "Они все надеются увидеть тебя там, понимаешь?"
    mc "И я вполне уверен, что ты всё ещё хочешь поговорить со мной."
    show monika 1br at t11 zorder 4
    window hide
    pause (2.0)
    show monika 1bp at f11 zorder 4
    m "И что после этого?"
    m "Ты все равно оставишь меня ради других девушек."
    show monika 1bo at t11 zorder 4
    mc "Никто не запрещает тебе быть с нами."
    show monika 2bg at f11 zorder 4
    m "Ты не понимаешь..."
    m "Всё, чего я хочу, это чтобы были только я и ты."
    m "Но ты не позволяешь мне это осуществить, ты хочешь больше быть с [persistent.sayoriname]."
    m "Ты заботишься о них, и я ничего не могу с этим поделать."
    m 1bg "Почему ты делаешь это со мной? Почему ты всё ещё приходишь сюда и пытаешься сделать так, чтобы мне стало лучше?"
    show monika 1bf at t11 zorder 4
    mc "Теперь уже ты не понимаешь."
    mc "Это не обязательно должны быть только ты и я, ты можешь быть счастливой со всеми нами вместе, всё, что тебе нужно, это попытаться."
    mc "И я пришёл сюда, потому что я тоже забочусь о тебе, я не хочу, чтобы ты чувствовала себя обделённой, и я, конечно же, не ненавижу тебя."
    mc "Но ты не можешь никого заставить любить тебя, бросать других только ради тебя, ты должна это знать."
    show monika 1bo at t11 zorder 4
    window hide
    pause (2.0)
    show monika 1bx at f11 zorder 4
    m "Всё ещё больно видеть вас с [persistent.sayoriname] такими."
    m "Я не хочу причинять ей боль, но и чувствовать себя так тоже не хочу!"
    show monika at thide zorder 4
    hide monika
    "Я вытираю её слезы и обнимаю её, пытаясь успокоить."
    mc "Она бы тоже не хотела, чтобы ты так себя чувствовала, поверь мне."
    m "..."
    m "[player],{w=0.5} не знаю, справлюсь ли я с этим..."
    mc "Но я знаю, что ты справишься, ты не можешь думать об этом вечно."
    mc "Ты намного выше этого."
    window hide
    pause (2.0)
    show monika 1bf at t11 zorder 4
    pause(1.5)
    mc "Увидимся позже, ладно?"
    show monika 2bp at f11 zorder 4
    m "Хорошо... тогда увидимся."
    show monika at thide zorder 4
    hide monika
    window hide
    pause (2.0)
    "Её чувства сегодня ещё более напряжённые."
    "Интересно, смогу ли я действительно помочь ей..."
    "Это скорее то, что она должна сделать с помощью одной лишь силы воли."
    "..."
    "Я всё ещё думаю о том, как помочь Нацуки, идти прямо к её дому – не самый лучший вариант."
    "Если я усилю своё внимание, я смогу увидеть, рядом она или нет."
    play sound Glow
    stop music fadeout 3.0
    window hide
    pause (3.0)
    "Я чувствую её присутствие за пределами любого здания, это хорошая возможность для меня."
    scene bg black with dissolve
    "Прежде чем она войдёт в любое другое здание, я бегу с безумной скоростью, чтобы догнать её."
    scene bg residential_day with dissolve_scene_full
    pause (1.0)
    "Так, ладно, сейчас я её догоню нормально."
    show natsuki 2bza at t11 zorder 4
    "Она замечает меня и оборачивается."
    show natsuki 1bd at f11 zorder 4
    play music t2
    n "О, привет, [player], что ты здесь делаешь?"
    show natsuki 1bj at t11 zorder 4
    mc "Я был у Моники сейчас, не думал, что встречу тебя здесь."
    mc "В любом случае, я хотел кое-что тебе предложить."
    show natsuki 1bza at t11 zorder 4
    "Когда я достаю ключи от дома, она смотрит на меня с растерянным лицом."
    show natsuki 1bc at f11 zorder 4
    n "Ты даёшь мне свои{w=0.25}.{w=0.25}.{w=0.25}. ключи?"
    show natsuki at t11 zorder 4
    mc "Ключи от моего дома, да."
    show natsuki 2bh at f11 zorder 4
    n "Ч-что?"
    n 2bq "Зачем ты мне это предлагаешь, я не хочу с тобой жить."
    show natsuki at t11 zorder 4
    mc "Сейчас я живу с [persistent.sayoriname], так что в данный момент домом никто не пользуется."
    show natsuki 1bk at t11 zorder 4
    "Как я и ожидал, её глаза почти мгновенно просветлели."
    mc "Это всё твоё, если хочешь, я действительно не против."
    mc "Сейчас там почти ничего нет, я уже перевёз все свои вещи."
    show natsuki 5bs at f11 zorder 4
    n "..."
    n 5bq "Я подумаю."
    show natsuki 5bs at t11 zorder 4
    mc "Конечно, не торопись, дай мне знать, когда решишь."
    mc "Увидимся на встрече!"
    show natsuki 2bl at f11 zorder 4
    n "Хорошо, увидимся!"
    show natsuki at thide zorder 4
    hide natsuki
    window hide
    pause (2.0)
    "Получилось лучше, чем я думал изначально."
    "Ее нерешительность может быть вызвана страхом перед последствиями, и в таком случае..."
    "Я должен был бы вмешаться, но это слишком рано."
    "Я должен вернуться домой до того, как это сделает [persistent.sayoriname]..."
    scene bg living_room with dissolve_scene_full
    pause (1.0)
    "[persistent.sayoriname] ещё не вернулась."
    "Было бы лучше, если бы я написал им сейчас."
    scene bg black with dissolve_scene_full
    scene bg living_room with dissolve_scene_full
    "Я слышу, как открывается дверь гостиной."
    show sayori 2bx at f11 zorder 4
    s "Я дома, [player]!"
    show sayori 4ba at t11 zorder 4
    mc "Хорошо, что ты купила?"
    show sayori 4bzb at f11 zorder 4
    s "Это сюрприз!"
    s 4bx "И не вздумай подглядывать!"
    show sayori 4ba at t11 zorder 4
    mc "Хорошо, хорошо, я не буду этого делать."
    show sayori 1ba at t11 zorder 4
    mc "Я всем написал, когда ты была там, они уже готовятся."
    mc "Это будет через несколько часов."
    mc "Хочешь поиграть в игры, пока мы ждём?"
    show sayori 4br at f11 zorder 4
    s "Конечно!"
    scene bg black with dissolve_scene_full
    "Мы играем несколько часов подряд, и ожидание закончилось, прежде чем мы это осознали."
    scene bg living_room with dissolve_scene_full
    "Кто-то звонит."
    mc "Ладно, [persistent.sayoriname], мы не должны заставлять их ждать."
    show sayori 2bx at t11 zorder 4
    s "Сейчас буду!"
    show sayori 4ba at t11 zorder 4
    mc "Хорошо."
    scene bg entrance with wipeleft_scene
    "Я подхожу к двери и открываю её, чтобы они вошли."
    show yuri 2bb at f11 zorder 4
    y "Эй, [player], мы здесь."
    show yuri 4ba at t21 zorder 3
    show natsuki 4ba at t22 zorder 4
    "Нацуки приносит поднос с кексами и чаем и отставляет его в сторону."
    n 5bd "У нас всё готово."
    n 5bc "Где [persistent.sayoriname]?"
    show natsuki at t22 zorder 4
    "Прежде чем я успеваю ей ответить, [persistent.sayoriname] бросается к нам и перебивает нас."
    show yuri at t31 zorder 2
    show natsuki 4ba at t32 zorder 3
    show sayori 4bp at f33 zorder 4
    s "Я здесь, извините!"
    s 5bb "Я хотела быстро закончить игру..."
    show sayori at t33 zorder 2
    show yuri 2bf at f31 zorder 4
    y "Я не знала, что ты играешь в видеоигры, [persistent.sayoriname]."
    show sayori 1ba at t33 zorder 4
    show yuri 2be at t31 zorder 2
    mc "Насколько я понимаю, она начала играть в них из-за меня."
    mc "Мы все могли бы попробовать это, по-моему, было бы довольно весело."
    show yuri 1bb at f31 zorder 4
    y "Конечно, почему бы и нет?"
    show yuri 1ba at t31 zorder 2
    show natsuki 5bd at f32 zorder 4
    n "Я готова к этому!"
    show natsuki 5ba at t32 zorder 3
    mc "И я полагаю, [persistent.sayoriname] согласна, это значит..."
    mc "Подожди, а где Моника?"
    show sayori 1bb at t33 zorder 3
    show yuri 1be at t31 zorder 1
    show natsuki 1bk at f32 zorder 4
    n "Мы не видели её по дороге сюда, может, она придёт позже?"
    show natsuki at t32 zorder 2
    mc "Ну... она сказала мне, что придёт, но если она не появится в ближайшее время, я пойду её искать."
    mc "Ребята, вам не о чем беспокоиться, пошли."
    "Я беру поднос с собой и иду в гостиную."
    scene bg living_room with wipeleft_scene
    pause (1.0)
    show sayori 1ba at t33 zorder 3
    show yuri 1ba at t31 zorder 1
    show natsuki 2bb at f32 zorder 4
    n "Будь осторожен с этим, я их долго делала!"
    show natsuki 2bc at t32 zorder 2
    mc "Я буду аккуратным, не беспокойся."
    "Я осторожно кладу его на ковер."
    mc "Таr, сейчас..."
    mc "[persistent.sayoriname], еда!"
    show sayori 4бм at f33 zorder 4
    s "Конечно!"
    s 2bx "Я скоро вернусь!"
    show yuri 1be at t31 zorder 1
    show natsuki 2bza at t32 zorder 2
    show sayori at thide zorder 4
    hide sayori
    "Когда [persistent.sayoriname] уходит за едой, кто-то начинает звонить."
    mc "Наверное, это Моника, я пойду за ней."
    scene bg entrance with wipeleft_scene
    pause(0.5)
    "Я открываю дверь."
    show monika 2bm at f11 zorder 4
    window hide
    pause (2.0)
    show monika 2bn at f11 zorder 4
    m "Привет..."
    show monika 2bm at t11 zorder 4
    "Возможно, я недооценил её, она нашла в себе силы появиться здесь."
    mc "Ты совсем немного опоздала, ничего не пропустила."
    mc "Тем не менее, рад видеть тебя здесь."
    show monika 1bg at f11 zorder 4
    m "Я не могла заставить себя не появиться."
    show monika 1bf at t11 zorder 4
    mc "Ну, заходи, они ждут тебя."
    show monika 1be at t11 zorder 4
    window hide
    pause(1.5)
    scene bg living_room with wipeleft_scene
    pause (1.0)
    show yuri 1ba at t21 zorder 1
    show natsuki 5bd at f22 zorder 2
    n "Явилась, не запылилась."
    show yuri at t31 zorder 1
    show natsuki 5ba at t32 zorder 2
    show monika 2bl at f33 zorder 3
    m "Извините за опоздание, у меня были неотложные дела."
    show monika at t44 zorder 3
    show yuri at t42 zorder 1
    show natsuki at t43 zorder 2
    show sayori 2bb at t41 zorder 4
    "[persistent.sayoriname] заходит в комнату, она удивлена, увидев здесь Монику."
    show sayori 4bx at f41 zorder 4
    s "Моника!"
    show sayori 4ba at t41 zorder 3
    show monika 1by at f44 zorder 4
    m "Привет, [persistent.sayoriname], рада тебя видеть."
    show sayori 2bzc at f41 zorder 4
    show monika 1be at t44 zorder 3
    s "Чувствуй себя как дома."
    s 1bx "Я готова принести закуски, так что, если ты проголодалась, поешь."
    show sayori 1ba at t41 zorder 3
    show monika 2bb at f44 zorder 4
    m "Спасибо, [persistent.sayoriname], я ценю твое предложение."
    m 1bn "Но я не такая уж голодная, может, попозже что-нибудь возьму."
    show monika 1бм at t44 zorder 3
    show sayori 2bx at f41 zorder 4
    s "Хорошо, я пойду за ними, это не займёт много времени."
    show sayori at thide zorder 4
    hide sayori
    window hide
    pause (2.0)
    show monika 1ba at t33 zorder 3
    show natsuki 2bd at f32 zorder 4
    show yuri at t31 zorder 1
    n "Итак, ребята, что вы хотите делать, когда наступит лето?"
    show natsuki 4ba at t32 zorder 2
    show yuri 2bj at f31 zorder 4
    y "Это очень неожиданный вопрос, Нацуки."
    y 1bb "Но я хочу прочитать несколько книг, которые я ещё не закончила, и я хочу провести время со всеми вами."
    y 4ba "Конечно, если вы свободны, я бы не хотела беспокоить вас, если вы слишком заняты."
    show yuri at t31 zorder 1
    show natsuki 4bz at f32 zorder 4
    n "Я совершенно свободна, так что с удовольствием!"
    show natsuki at t32 zorder 2
    show monika 2bb at f33 zorder 3
    m "На данный момент у меня нет никаких планов, я подумаю об этом в другой раз."
    m "А что насчет тебя, [player]?"
    show monika 4ba at t33 zorder 3
    mc "Я?"
    mc "..."
    mc "Я хочу решить проблему, которая у меня есть, до лета, я хочу сделать это, чтобы я мог расслабиться."
    show monika 2bc at t33 zorder 3
    show natsuki 1bk at f32 zorder 4
    show yuri 1be at t31 zorder 1
    n "В чём проблема? Мы могли бы тебе помочь."
    show natsuki 1bza at t32 zorder 2
    mc "Нет, все в порядке, тебе не о чем беспокоиться."
    "Пока..."
    show yuri 1bf at f31 zorder 4
    y "[player], если тебе нужна помощь, обратись к нам."
    show natsuki 5ba at t32 zorder 2
    y 1bb "Мы готовы тебе помочь."
    show yuri 1ba at t31 zorder 4
    mc "Спасибо, я буду иметь это в виду."
    mc "Но кроме этого, я думаю, что [persistent.sayoriname] готова принести еду."
    show yuri 1be at t31 zorder 1
    show natsuki 1bza at t32 zorder 2
    "Как только я заканчиваю это предложение, [persistent.sayoriname] медленно приближается к нам с едой, которую едва может удержать."
    show yuri 1bn at h31 zorder 1
    show natsuki 1bp at h32 zorder 2
    show monika 1bd at t33 zorder 3
    "Она бросает всё это на пол."
    show sayori 4бр at t41 zorder 4
    show yuri 1bn at t42 zorder 1
    show natsuki 1bp at t43 zorder 2
    show monika 1bd at t44 zorder 3
    s "Это всё!"
    show sayori 1ba at t41 zorder 3
    show yuri 2bq at f42 zorder 4
    y "[persistent.sayoriname], не слишком ли это?"
    show sayori 1bb at t41 zorder 3
    y "Я не уверена, что мы сможем всё это съесть."
    show yuri 2by at t42 zorder 1
    show sayori 2bx at f41 zorder 4
    show natsuki 1bi at t43 zorder 2
    s "Не волнуйся, я могу оставить немного на следующий раз, если мы не закончим сегодня."
    s 1bx "Итак, ребята, как насчет того, чтобы попробовать видеоигры?"
    show sayori 1ba at t41 zorder 4
    show yuri 2bc at t42 zorder 1
    show natsuki 4ba at t43 zorder 2
    show monika 1ba at t44 zorder 3
    "Все весело кивают, и мы все начинаем играть в игры."
    scene bg black with dissolve_scene_full
    "Кажется, им всем это нравится, это меня немного удивило."
    "Кто бы мог подумать, что они, несмотря на интерес к литературе, могут заинтересоваться видеоиграми?"
    "Через некоторое время Моника шепчет мне, показывая, что хочет поговорить."
    "Мы говорим остальным, что скоро вернёмся."
    stop music fadeout 2.5
    scene bg house_corridor с dissolve_scene_full
    pause(1.5)
    show monika 1be at t11 zorder 4
    play music Eternity2
    "Моника улыбается мне, когда мы оба сидим у стены."
    mc "Приятно быть с ними, не так ли?"
    show monika 2bn at f11 zorder 4
    m "Да, они действительно хорошие люди."
    m 1bk "В конце концов, это было правильное решение."
    show monika 1bj at t11 zorder 4
    "Сомнительно, притворяется ли она, что так думает, или это на самом деле так."
    mc "Итак... Я хотел спросить тебя кое о чём."
    show monika 1bc at t11 zorder 4
    mc "Теперь, когда я думаю об этом, разве не должен был быть какой-то фестиваль?"
    show monika 1bo at t11 zorder 4
    "Она молчит, как я и думал."
    mc "Ты так беспокоилась обо мне, что даже не удосужилась сказать им, верно?"
    show monika 1bf at f11 zorder 4
    m "..."
    m 1bg "Да..."
    m "Я не сообщила им об этом, вся ситуация между нами выбила меня из колеи."
    m "И я не думаю, что подготовка к фестивалю облегчит это."
    show monika 1bf at t11 zorder 4
    mc "Это понятно, к тому же..."
    mc "Я считаю, что мы можем быть хорошим клубом, как сейчас, зачем нам больше участников?"
    show monika 1by at f11 zorder 4
    m "В этом ты прав."
    m 2bn "Честно говоря, я даже не знаю, будет ли кому-то интересно присоединиться."
    show monika 2bm at t11 zorder 4
    "Между нами минута молчания."
    "Я изо всех сил пытаюсь понять, что она думает по этому поводу."
    mc "Моника."
    show monika 1bc at t11 zorder 4
    mc "Я понимаю, почему ты пыталась сделать всё это, всё{w=0.25}.{w=0.25}.{w=0.25}. сама знаешь что."
    show monika 1bf at t11 zorder 4
    mc "Но ты должна понять, почему я не позволяю тебе делать это сейчас."
    mc "Ты выше этого, я знаю."
    show monika at f11 zorder 4
    m "..."
    m 1bg "А лучше ли, [player]?"
    m "Я даже не понимаю, что я к тебе чувствую..."
    show monika 1bf at t11 zorder 4
    mc "Эй, подожди немного и подумай."
    mc "Я пришёл сюда не для того, чтобы причинять тебе боль, наоборот, я знаю, что ты не хочешь этого."
    mc "Но заставить меня сосредоточить внимание на тебе и только на тебе?"
    mc "Это неправильно, Моника."
    show monika 2bp at f11 zorder 4
    m "Я знаю, я знаю..."
    m 2бо "..."
    m 1bg "[player], я прошу прощения за то, что хотела сделать."
    m "Как я пыталась помешать тебе спасти жизнь [persistent.sayoriname]..."
    m 1bx "Я должна желать тебе лучшего, но всё, что я сделала, сделало только хуже."
    show monika 1bw at t11 zorder 4
    "Я держу её руки, замечая легкую дрожь, исходящую от неё."
    mc "Все в порядке, Моника."
    mc "По крайней мере, ты наконец это осознаёшь, и это хорошо для нас обоих."
    mc "Я не хочу сражаться с тобой, поэтому, пожалуйста... не заставляй меня это делать."
    show monika 1bz at t11 zorder 4
    window hide
    pause (2.0)
    show monika 2by at f11 zorder 4
    m "Хорошо, я сделаю для тебя всё, что смогу."
    m 2bg "Но я ничего не могу тебе обещать."
    show monika 2bf at t11 zorder 4
    mc "Тем не менее, я понимаю, надеюсь, у тебя всё будет хорошо."
    mc "Помни, я здесь ради тебя, и я помогу тебе."
    mc "Даже если это кажется невозможным."
    show monika 2be at t11 zorder 4
    window hide
    pause(2.2)
    show monika 1bd at f11 zorder 4
    m "[player], у меня к тебе вопрос."
    m "Как ты думаешь, возможно ли перенести меня в реальный мир?"
    show monika 1bc at t11 zorder 4
    mc "Зачем тебе туда идти?"
    mc "Этот мир больше ни к чему не привязан, кроме..."
    mc "Путешествие по мирам – дело непростое, на это уходит много энергии."
    mc "Взять туда кого-угодно было бы сложно, даже для меня."
    show monika 1bf at t11 zorder 4
    mc "Я не говорю, что этого не может быть, но ничего страшного, если мы пока останемся здесь."
    show monika 2bo at t11 zorder 4
    window hide
    pause (2.0)
    show monika 2bp at f11 zorder 4
    m "Да, думаю, ты прав."
    m 1bg "Я не хотела бы рисковать тем, чтобы ты из-за этого пострадал."
    show monika 1bf at t11 zorder 4
    mc "В худшем случае я буду лишён энергии."
    mc "Если бы это было выше моих сил, то я бы вообще не смог этого сделать."
    mc "Тебе не о чем беспокоиться, Моника."
    show monika 1be at t11 zorder 4
    window hide
    pause (2.0)
    show monika 2by at f11 zorder 4
    m "Какое облегчение."
    m 2bb "Но я думаю, это не так уж и удивительно, учитывая то, на что ты способен."
    show monika 2ba at t11 zorder 4
    mc "Ты и половины не видела."
    mc "Даже люди из моего собственного мира боятся моих способностей."
    show monika 1bc at t11 zorder 4
    mc "Надеюсь, тебе никогда не придётся увидеть..."
    mc "Извини, я не должен говорить об этом во время нашего разговора."
    show monika 1by at f11 zorder 4
    m "Всё в порядке, [player], правда."
    m "Я очень благодарна, что ты захотел поговорить со мной, несмотря на всё, что я сделала."
    m 1bg "Я даже этого не заслуживаю."
    show monika 1bf at t11 zorder 4
    mc "Да ладно, мы все делаем ошибки, это естественно."
    mc "Но важно, чтобы ты не сожалела, вместо этого ты должна сосредоточиться на том, что ты можешь изменить."
    mc "Размышления о прошлом только угнетают тебя, понимаешь?"
    show monika 2bn at f11 zorder 4
    m "Что-то вроде этого должно исходить от меня, ха-ха."
    m 2bd "Теперь, когда я думаю об этом..."
    m 1bd "[player], ты в курсе..."
    show monika 1bc at t11 zorder 4
    mc "В курсе чего?"
    show monika 2bn at f11 zorder 4
    m "Немного странно говорить об этом."
    m 2bd "Но, может быть, ты знаешь, раз ты, наверное, знаешь об этом месте всё."
    m 1bg "Человек, наблюдающий за нами... он всё ещё может причинить нам вред?"
    show monika 1bf at t11 zorder 4
    mc "Не беспокойся, он ничего не может сделать ни мне, ни тебе, ни им."
    mc "Он не может противостоять мне."
    mc "Кем бы он ни был, это не меняет того факта, что я полностью контролирую себя и этот мир."
    show monika 2bl at f11 zorder 4
    m "Это меня радует."
    m 1bd "Тем не менее, я никогда бы не подумала, что ты сможешь пересечь границу."
    m 1by "Это почти как сбывшаяся мечта."
    m 1bp "За исключением того, что ты..."
    show monika 1bo at t11 zorder 4
    mc "Я знаю, что ты хочешь, чтобы я любил тебя и отвергал других."
    mc "Но ты должна уважать мой выбор, я люблю [persistent.sayoriname]."
    show monika 1bp at f11 zorder 4
    m "Эти слова словно копьё пронзают мое сердце."
    m 1bg "Я ничего не могу с этим поделать, [player]."
    show monika 1bf at t11 zorder 4
    mc "Моника, я знаю, что ты способна на это."
    mc "В тебе есть это, и я это знаю."
    mc "Наберись терпения, ты почувствуешь себя намного лучше, когда ты это отпустишь."
    mc "Поверь мне, у меня была похожая ситуация в прошлом."
    mc "Была группа, которую я возглавлял, я старался, чтобы всем было весело."
    mc "В конце концов, они все разошлись, и все мои усилия пошли прахом."
    mc "В моём сердце появилась ненависть, я тоже не мог отпустить её."
    mc "Но, в конце концов, я принял это и живу дальше, и теперь я здесь, на меня это больше не влияет."
    show monika 1bg at f11 zorder 4
    m "[player]..."
    m "Я{w=0.25}.{w=0.25}.{w=0.25} я не знаю, что сказать..."
    show monika 1bf at t11 zorder 4
    mc "Всё в порядке, тебе не нужно ничего говорить."
    show monika at thide zorder 4
    hide monika
    "Она притягивает меня, чтобы обнять."
    "Я почти чувствую силу её эмоций, бедная Моника."
    "Даже она не заслуживает этого, несмотря на то, что она сделала."
    "Я действительно не могу злиться на неё, даже если у меня есть на это все основания."
    show monika 1be at t11 zorder 4
    "Она медленно вырывается."
    mc "Надеюсь, это помогло тебе немного очистить свой разум."
    show monika 1by at f11 zorder 4
    m "Так и было."
    m "Большое спасибо, [player]."
    show monika 1be at t11 zorder 4
    mc "В любое время!"
    mc "Может, нам стоит вернуться?"
    show monika 2bb at f11 zorder 4
    m "Ага!"
    stop music fadeout 2.0
    scene bg living_room_late with dissolve_scene_full
    "[persistent.sayoriname] замечает, что мы возвращаемся, и быстро приближается к нам."
    show sayori 2bx at f11 zorder 4
    play music t2
    s "Ты вернулся! Как всё прошло?"
    show sayori 4ba at t22 zorder 4
    show monika 1be at t21 zorder 4
    mc "Мы долго разговаривали, это было довольно освежающе."
    show sayori 1bzc at f22 zorder 4
    s "Тебе лучше, Моника?"
    show sayori 1bd at t22 zorder 3
    show monika 2bk at f21 zorder 4
    m "Да! [player] и я поговорили по душам, и теперь мне легче."
    m "Он помог мне избавиться от стресса."
    show monika at thide zorder 4
    hide monika
    show sayori at thide zorder 3
    hide sayori
    "Мы все возвращаемся к игре, но вскоре после этого я замечаю выражение лица [persistent.sayoriname]."
    show sayori 1bk at t11 zorder 4
    "Она смотрит в пол с грустным выражением лица."
    mc "[persistent.sayoriname], ты в порядке?"
    show sayori 1bzc at f11 zorder 4
    s "Я просто чувствую себя немного подавленной."
    s "Тебе не о чем волноваться!"
    show sayori 1bd at t11 zorder 4
    mc "Нет, это важно, я это вижу."
    show sayori 1bg at t11 zorder 4
    mc "Давай, я скажу им, что нам нужно кое о чём поговорить."
    show sayori 2bh at f11 zorder 4
    s "Тебе действительно не нужно этого делать, [player]."
    show sayori 2bg at t11 zorder 4
    mc "То, как ты себя чувствуешь, гораздо важнее."
    mc "Пожалуйста, не отбрасывай это."
    stop music fadeout 3.0
    scene bg black with dissolve_scene_full
    "Я всем говорю, что нам с [persistent.sayoriname] нужно кое-что обсудить наедине."
    "Мы идем в её спальню, они не могут услышать, о чём мы говорим."
    scene bg sayori_bedroom_late с dissolve_scene_full
    pause (1.0)
    show sayori 1bg at t11 zorder 4
    "Судя по тому, как она смотрит на меня, я думаю, что знаю, о чём идет речь."
    mc "[persistent.sayoriname], это из-за твоей депрессии?"
    show sayori at f11 zorder 4
    s "..."
    play music t10
    s 2bh "Я не могу перестать думать об этом..."
    s "И я должна веселиться со всеми вами."
    show sayori 2bg at t11 zorder 4
    window hide
    pause (2.0)
    show sayori 1bk at f11 zorder 4
    s "[player], почему ты хочешь быть со мной?"
    s 1bh "Тебе лучше быть с ними, я просто тяну тебя на дно со своими чувствами."
    show sayori 1bg at t11 zorder 4
    mc "Я даже не могу объяснить, как ты важна для меня, [persistent.sayoriname]."
    mc "И я хочу сделать всё, что в моих силах, чтобы помочь тебе, сколько бы времени это ни заняло."
    mc "Будь то месяцы, годы, вечность."
    mc "Я сделаю всё, что смогу, потому что я люблю тебя, [persistent.sayoriname]."
    show sayori 2bv at f11 zorder 4
    s "..."
    s "[player], я тебя не заслуживаю, я тебя совсем не заслуживаю."
    show sayori 2бу at t11 zorder 4
    mc "Нет, ты меня заслуживаешь."
    mc "Если они заслуживают меня, то почему бы и нет?"
    mc "Ты милая, добрая и заботливая, и ты обращалась со мной лучше, чем кто-либо другой."
    mc "Несмотря на всё, что было брошено на тебя, ты осталась со мной."
    mc "Если это не доказывает, что ты меня заслуживаешь, тогда что?"
    show sayori 1bv at f11 zorder 4
    s "Ты... серьезно?"
    show sayori at t11 zorder 4
    mc "Конечно, это просто кто ты есть, [persistent.sayoriname]."
    mc "Я бы не хотел, чтобы ты была какой-то другой."
    mc "Ты идеальна такой, какой ты есть."
    show sayori 2bv at f11 zorder 4
    s "Но, [player], ты должен был сегодня повеселиться."
    s "И вместо этого ты снова здесь и слушаешь мою проблему."
    show sayori 2bk at f11 zorder 4
    s "Я сейчас всё испорчу!"
    show sayori at t11 zorder 4
    mc "Нет, это не так."
    mc "Я не хочу жить без тебя, поэтому, что бы мне ни пришлось пережить, я вынесу это с тобой."
    show sayori 1bh at f11 zorder 4
    s "Но..."
    s 1bg "..."
    show sayori 1bg at t11 zorder 4
    mc "Пока я могу заставить тебя чувствовать себя лучше, пусть даже немного, мне достаточно сделать этот шаг."
    show sayori 1bk at f11 zorder 4
    s "[player]..."
    s 2bh "У меня до сих пор в голове те мысли, которые говорят мне сомневаться в твоих словах."
    s "Как бы я ни старалась, я не могу перестать думать об этом."
    s 4bw "Я должна быть счастливой! Почему серые тучи не исчезают?!"
    show sayori at thide zorder 4
    hide sayori
    "Я притягиваю её для крепких объятий, все громче слыша её неудержимые рыдания."
    "Это разбивает мне сердце, когда я вижу, как она так страдает."
    mc "Я знаю, что это займёт много времени, потому что кажется, что это никогда не закончится."
    mc "Но, [persistent.sayoriname], не забывай, что я всегда рядом с тобой."
    mc "Я не считаю тебя обузой, и ты определённо не бесполезна."
    mc "Ты помогла мне почувствовать, что я принадлежу этому месту, и это имеет истинную ценность в моём сердце, хочешь верь, хочешь нет."
    show sayori 1bu at t11 zorder 4
    "Она теряет дар речи, но могу ли я её винить?"
    "Её мысли подавлены эффектом депрессии."
    "Это заставляет меня по-настоящему оценить своё психическое состояние."
    show sayori 1bv at f11 zorder 4
    s "[player], я знаю, ты сказал мне, что всё будет хорошо."
    s "Но что, если я никогда не поправлюсь?"
    show sayori at t11 zorder 4
    mc "Тебе станет лучше, потому что ты сильная, [persistent.sayoriname]."
    mc "Вспомни, чего ты уже успела добиться!"
    mc "Я верю в тебя, у тебя есть всё, что нужно, чтобы побороть эти тучки."
    show sayori 2bv at f11 zorder 4
    s "Ты{w=0.25}.{w=0.25}.{w=0.25}. действительно так думаешь?"
    show sayori at t11 zorder 4
    mc "Да, ты уже показывала мне это."
    mc "Не сомневайся в себе, я верю в тебя, как и все остальные."
    show sayori 1bt at t11 zorder 4
    window hide
    pause(2.5)
    show sayori 1bzd at f11 zorder 4
    s "Я действительно так много для тебя значу, не так ли?"
    show sayori 1bt at t11 zorder 4
    mc "Ты значишь для меня всё, даже если ты никогда не перестанешь так думать."
    mc "Тогда, по крайней мере, ты будешь не одна."
    show sayori 3bv at f11 zorder 4
    s "[player]..."
    s "Ты не обязан делать это для меня."
    show sayori at t11 zorder 4
    mc "Но я буду, это моё решение."
    mc "Пока я могу быть с тобой и защищать тебя, я буду это делать."
    mc "[persistent.sayoriname]..."
    mc "Ты заполнила пустую дыру внутри меня, я не знал, что мне это нужно."
    mc "Никто не понимает меня лучше тебя, даже если ты так не думаешь."
    mc "Пожалуйста... позволь мне сделать это для тебя."
    show sayori 1bt at t11 zorder 4
    window hide
    pause (2.0)
    show sayori 2bzd at f11 zorder 4
    s "У меня действительно нет выбора, не так ли?"
    s 1bzd "Мне приятно, когда ты заботишься обо мне."
    s 2bv "Но иногда мне кажется, что ты тратишь на меня свои силы зря."
    show sayori at t11 zorder 4
    mc "Я точно знаю, что не трачу свои силы зря."
    mc "Я дам тебе столько времени, сколько тебе нужно, мы не обязаны возвращаться прямо сейчас."
    show sayori 1bt at t11 zorder 4
    window hide
    pause (2.0)
    show sayori 2bzc at f11 zorder 4
    s "Ничего, если мы немного отдохнем здесь?"
    show sayori 2bd at t11 zorder 4
    mc "Да, они могут подождать."
    scene bg black with dissolve_scene_full
    "Мы ложимся спать и обнимаем друг друга."
    window hide
    pause (2.0)
    scene bg sayori_bedroom_late с dissolve_scene_full
    show yuri 1be at t11 zorder 4
    "Когда я начинаю просыпаться, я вижу Юри, стоящую там."
    mc "Юри?"
    show yuri 2bn at f11 zorder 4
    y "Ой! Извини!"
    y 4bb "Я не хотела тебя будить."
    show yuri at t11 zorder 4
    mc "Нет, все в порядке."
    mc "Вероятно, ты беспокоилась о нас, поэтому пришла сюда, чтобы убедиться сама."
    show yuri 1bt at t21 zorder 3
    show sayori 2bb at f22 zorder 4
    s "О... привет, Юри."
    s 1bl "Это... довольно неловко."
    s 1bh "Извини, что ничего тебе не сказала."
    show sayori 1bg at t22 zorder 3
    show yuri 1bu at f21 zorder 4
    y "Всё в порядке, [persistent.sayoriname]."
    y 2bt "Полагаю, это как-то связано с твоей депрессией?"
    show yuri 2bzg at t21 zorder 3
    show sayori at f22 zorder 4
    s "..."
    s 2bh "Да, [player] и я говорили об этом."
    s 1bzc "Но всё в порядке, я чувствую себя лучше после разговора с ним."
    show sayori 1bd at t22 zorder 3
    show yuri 1bzi at f21 zorder 4
    y "Нам очень повезло, что у тебя есть такой человек, как [player]."
    show yuri 1bs at t21 zorder 3
    "Это почти заставляет меня чувствовать, что она ревнует."
    "Но я знаю, что Юри – понимающий человек."
    "Она хочет только лучшего для [persistent.sayoriname], как и я."
    show sayori 2br at f22 zorder 4
    s "Я тоже так думаю!"
    s 2bzc "Я не могу не отблагодарить его, он так много сделал для меня."
    show sayori 2bd at t22 zorder 4
    mc "[persistent.sayoriname], ты тоже много для меня сделала."
    mc "Я люблю тебя."
    show sayori 4bzc at f22 zorder 4
    s "Я тоже люблю тебя, [player]."
    show sayori 4bd at t22 zorder 4
    show yuri 4bb at t21 zorder 3
    "Инстинктивно я замечаю, как Юри к этому относится."
    show sayori 1bb at t22 zorder 4
    "Я смотрю на [persistent.sayoriname], показывая, что хочу взглянуть на Юри."
    window hide
    pause(1.5)
    show sayori 1bg at t22 zorder 4
    pause(1.5)
    show sayori 2bh at f22 zorder 4
    s "Юри?"
    s "Ты не{w=0.25}.{w=0.25}.{w=0.25}. ревнуешь, да?"
    show sayori 2bg at t22 zorder 3
    show yuri 2bn at f21 zorder 4
    y "Ч-что?!"
    y 1bq "С ума сошла? Что навело тебя на эту мысль?"
    show yuri at t21 zorder 3
    show sayori 1bh at f22 zorder 4
    s "Я вижу это на тебе, Юри."
    show sayori 1bg at t22 zorder 3
    show yuri 2bzi at f21 zorder 4
    y "Н-нет, я очень рада за вас двоих."
    y 2bv "Кроме того, вы и так уже имеете дело с достаточным количеством проблем, я не хочу добавлять вам ещё больше."
    show yuri at t21 zorder 3
    show sayori 1bf at t22 zorder 4
    "Думаю, я должен был ожидать, что это произойдёт."
    "Её случай немного похож на случай Моники, но пока не такой тяжёлый."
    mc "[persistent.sayoriname], Юри, как насчёт того, чтобы потусить как-нибудь? Только втроём."
    show yuri 1be at t21 zorder 3
    show sayori 2bx at f22 zorder 4
    s "Ага! Хорошая идея!"
    show sayori 4ba at t22 zorder 3
    show yuri 1bq at f21 zorder 4
    y "Всё в порядке, ребята."
    y 1bf "Но нам пора возвращаться, они, наверное, волнуются."
    show yuri 1be at t21 zorder 3
    show sayori 1bh at f22 zorder 4
    s "Верно, мы здесь уже довольно давно."
    show sayori 1bg at t22 zorder 4
    mc "Тогда давай."
    mc "Мы не должны заставлять их ждать ещё дольше."
    show yuri 1ba at t21 zorder 3
    show sayori 1ba at t22 zorder 4
    "Они оба кивают, и мы выходим из комнаты."
    stop music fadeout 2.5
    scene bg living_room_late with dissolve_scene_full
    pause (1.0)
    show sayori 2bl at f11 zorder 4
    play music t8
    s "Мы здесь! Извините, это заняло больше времени, чем я думала."
    show sayori at t33 zorder 3
    show monika 1ba at t31 zorder 2
    show natsuki 4bl at f32 zorder 4
    n "Наконец-то!"
    n 5bk "Почему так долго?"
    show natsuki 5bzа at t32 zorder 4
    mc "[persistent.sayoriname] плохо себя чувствовала, поэтому ей пришлось немного вздремнуть."
    show natsuki 1bc at f32 zorder 4
    n "Вы вздремнули... вместе?"
    show natsuki at t32 zorder 3
    show sayori 5bb at f33 zorder 4
    s "Хе-хе... да."
    show sayori at t33 zorder 3
    show monika 1bf at t31 zorder 2
    show natsuki 5by at f32 zorder 4
    n "Вы двое просто не можете быть друг без друга, не так ли?"
    show sayori 1bq at t33 zorder 3
    show natsuki at t32 zorder 4
    "Я издал небольшой смешок."
    "Несмотря на то, что она так отреагировала, Нацуки, кажется, совсем не возражает."
    "Но я не могу сказать то же самое о Монике..."
    "Как будто она никогда не справится с этим."
    show monika at t41 zorder 1
    show natsuki 1bza at t42 zorder 2
    show sayori 1bb at t43 zorder 3
    show yuri 2bb at f44 zorder 4
    y "Думаю, мы можем на этом закончить."
    y 1bd "Сегодня было очень приятно! Большое всем спасибо."
    show sayori 2bzc at f43 zorder 4
    show yuri 1bc at t44 zorder 2
    show natsuki 1ba at t42 zorder 2
    s "Ой, не говори об этом, Юри!"
    s 2bx "Мы можем ещё как-нибудь потусить."
    show yuri 1ba at t44 zorder 2
    show sayori 1ba at t43 zorder 3
    mc "Я всегда свободен, так что всё зависит от вас."
    show monika 2bn at f41 zorder 4
    m "Думаю, я смогу найти немного времени на следующей неделе."
    m 2bd "Но я ничего не обещаю."
    show monika 2bc at t41 zorder 3
    show natsuki 5bq at f42 zorder 4
    n "Уф, мне придётся снова обсудить это с отцом."
    show yuri 1be at t44 zorder 2
    show sayori 1bb at t43 zorder 3
    n "Было так трудно убедить его отпустить меня."
    n 1bc "Но я сделаю всё, что смогу."
    show natsuki at t42 zorder 2
    "Я поговорю об этом с Нацуки."
    "Она должна сопротивляться контролю своего отца, и я помогу ей в этом."
    mc "Тогда, думаю, мы увидимся на следующей неделе."
    show yuri 2bd at f44 zorder 4
    show sayori 1ba at t43 zorder 3
    show natsuki 5ba at t42 zorder 2
    y "Уже с нетерпением жду этого!"
    y 1bb "Но я уже выхожу, увидимся в понедельник."
    show natsuki 1bc at f42 zorder 4
    show yuri 1ba at t44 zorder 2
    n "Я тоже ухожу, увидимся позже!"
    show monika 1ba at t21 zorder 3
    show sayori 2bq at t22 zorder 4
    show natsuki at thide zorder 4
    hide natsuki
    show yuri at thide zorder 4
    hide yuri
    "Мы машем им, когда они уходят."
    show sayori 2bzc at f22 zorder 4
    s "Надеюсь, тебе было весело, Моника."
    show sayori 2bd at t22 zorder 3
    show monika 2bn at f21 zorder 4
    m "Мы никогда раньше не делали ничего подобного, это было для меня в новинку."
    m 2bd "Честно говоря, я не знала, чего ожидать."
    m 1by "Сначала я даже не хотела идти, но [player] убедил меня попробовать."
    m "И я рада, что я передумала, это было так освежающе."
    show monika 1be at t21 zorder 3
    show sayori 4br at f22 zorder 4
    s "Ура!!"
    s 2bx "Если вам весело, это главное!"
    show sayori 4ba at t22 zorder 3
    show monika 2br at f21 zorder 4
    m "Однако мне всё равно нужно позаботиться обо всей работе."
    show monika 2bq at t21 zorder 3
    show sayori 2bb at t22 zorder 4
    mc "Мы сказали тебе, что справимся с этим, на этот раз тебе не о чем беспокоиться."
    show monika 1bg at t21 zorder 3
    show sayori 1bzc at f22 zorder 4
    s "Да! Оставь это нам, Моника."
    s "Я обещала тебе, что тебе не придётся этого делать."
    show sayori 1bd at t22 zorder 3
    show monika 2by at f21 zorder 4
    m "Всё в порядке, тебе действительно не нужно."
    m "Я к этому привыкла, меня это совсем не беспокоит."
    show monika 2be at t21 zorder 3
    show sayori 2bg at t22 zorder 4
    mc "Моника, ты заслужила выходной."
    mc "Ты очень много работала, не чувствуй себя виноватой за то, что ничего не делала целый день."
    show sayori 2bh at f22 zorder 4
    s "Точно!"
    s 2bzc "Пожалуйста, просто позволь нам сделать это вместо тебя."
    show sayori 2bd at t22 zorder 3
    show monika 1bo at f21 zorder 4
    m "..."
    m 1bn "Возражения, как я полагаю, не принимаются?"
    show monika 1bm at t21 zorder 3
    show sayori 1bq at t22 zorder 4
    "Мы с [persistent.sayoriname] качаем головами."
    show sayori 1ba at t22 zorder 3
    show monika 2bl at f21 zorder 4
    m "Думаю, ты прав, может, мне стоит взять выходной."
    m 2bb "Если ты действительно настаиваешь, то я передам тебе все бумаги."
    show sayori 1bx at f22 zorder 4
    show monika 2ba at t21 zorder 3
    s "Мы сделаем это раньше, чем ты успеешь!"
    s 2bc "Но есть один нюанс..."
    s 1bl "Где они у тебя?"
    show sayori at t22 zorder 3
    show monika 2bd at f21 zorder 4
    m "О... {w=0.6}{nw}"
    extend 1bg "извините, я забыла взять их с собой."
    show monika 1bf at t21 zorder 3
    show sayori 1bb at t22 zorder 4
    mc "Всё в порядке, я могу навестить тебя и забрать их завтра."
    show sayori 1ba at t22 zorder 3
    show monika 4bb at f21 zorder 4
    m "В таком случае решено!"
    m 1by "Большое спасибо вам двоим за сегодняшний день и за помощь в работе."
    show monika 1be at t21 zorder 4
    mc "Не за что, Моника."
    mc "Тогда увидимся завтра!"
    show monika 2bb at f21 zorder 4
    m "Да, увидимся завтра!"
    show monika at thide zorder 4
    hide monika
    show sayori 1bq at t22 zorder 4
    "Моника уходит."
    show sayori 1ba at t11 zorder 4
    mc "Итак, [persistent.sayoriname], как насчёт того, чтобы посмотреть фильм?"
    show sayori 2br at f11 zorder 4
    s "Конечно! Почему бы и нет?"
    s 2bx "Что бы ты хотел посмотреть?"
    show sayori 4ba at t11 zorder 4
    mc "Мне нравятся боевики, с драками и сверхъестественными способностями."
    show sayori 1bl at f11 zorder 4
    s "Это очень похоже на тебя, хе-хе..."
    s 1bx "Но я не против, это может быть весело!"
    show sayori 1ba at t11 zorder 4
    mc "Ладно тогда!"
    scene bg black with dissolve_scene_full
    stop music fadeout 3.0
    "На этот раз ничто не беспокоило нас, пока мы смотрели."
    "С моей волей я смог сопротивляться всем видениям, которые у меня были раньше, и до сих пор ничего не произошло."
    "Уже поздно, и после фильма мы решаем лечь спать."
    scene bg house_corridor_night with dissolve_scene_full
    pause (1.0)
    "Прежде чем я потянусь к ручке двери, [persistent.sayoriname] быстро хватает меня за руку."
    show sayori 3pc at f11 zorder 4
    s "[player], пока ты не ушёл..."
    s 3py "..."
    s "Можем ли мы{w=0.25}.{w=0.25}.{w=0.25}. снова поспать рядом друг с другом?"
    show sayori at t11 zorder 4
    mc "..."
    mc "Я на самом деле хотел задать тебе тот же вопрос, ха-ха."
    show sayori 1pe at t11 zorder 4
    mc "Да, я был бы более чем счастлив."
    show sayori 4ps at t11 zorder 4
    "Она одаривает меня яркой улыбкой и тащит в свою комнату."
    scene bg black with dissolve_scene_full
    "Её улыбка – это все, что я хочу видеть."
    "Её безопасность – это всё, что я хочу защитить."
    "И для этого я должен решить это как можно скорее."
    pause(2.0) #Конец главы 3: Решение и осуждение ###################################### ################################################### #####################################
    scene bg Chapter4 with dissolve_scene_full
    pause (3.0)
    scene bg sayori_bedroom with dissolve_scene_full
    pause (1.0)
    "Я медленно начинаю просыпаться."
    "Было бы удобно, если бы я сегодня поговорил с Нацуки о её отце."
    "Но как мне это сделать? Я не думаю, что появляться перед её домом – хорошая идея…"
    "Мне придется подождать, пока она будет где-то ещё..."
    show sayori 4pza at t11 zorder 4
    "О... [persistent.sayoriname] просыпается."
    "Она такая красивая, моё сердце всегда согревается, когда я вижу её."
    play music t2
    mc "Доброе утро, [persistent.sayoriname]."
    show sayori 1pzc at f11 zorder 4
    s "Доброе утро!"
    s 1pr "Не думай, что сегодня ты пропустишь завтрак!"
    show sayori 1pq at t11 zorder 4
    mc "Ха-ха, как я мог?"
    mc "Кроме того... Я увижу, как ты улыбаешься, если я всё-таки не пропущу."
    show sayori 1pe at f11 zorder 4
    s "..."
    s 1ps "В таком случае, я буду улыбаться каждое утро."
    s 2px "Ты больше никогда не будешь пропускать завтрак таким образом!"
    show sayori 2pa at t11 zorder 4
    mc "Такая ты подлая девчонка, [persistent.sayoriname]."
    show sayori 4pq at t11 zorder 4
    "Она хихикает и весело выводит меня из комнаты."
    scene bg living_room with dissolve_scene_full
    pause (1.0)
    show sayori 2bc at f11 zorder 4
    s "[player], я должна была спросить тебя об этом раньше, но..."
    s 1bc "Что ты предпочитаешь есть?"
    show sayori 1bb at t11 zorder 4
    mc "На завтрак?"
    mc "Ну... всё, что не сухое: например, хлопья."
    mc "Я очень не люблю тяжёлую пищу так рано утром."
    show sayori 1bc at f11 zorder 4
    s "А как насчёт бекона и яиц?"
    show sayori 1bb at t11 zorder 4
    mc "Я бы не возражал против бекона, но я не люблю яйца."
    show sayori at f11 zorder 4
    s "О..."
    s 2br "Ничего, тогда я приготовлю тебе хлопья!"
    show sayori 2bq at t11 zorder 4
    mc "Хорошо!"
    scene bg living_room with dissolve_scene_full
    pause (1.0)
    show sayori 1bx at f11 zorder 4
    s "Вот твои хлопья!"
    show sayori 1ba at t11 zorder 4
    mc "Они выглядят красиво, а также сильно отличаются от тех, что я привык есть."
    mc "Спасибо, [persistent.sayoriname]."
    show sayori 1bzc at f11 zorder 4
    s "Пожалуйста."
    show sayori 2bb at f11 zorder 4
    stop music fadeout 2.0
    s "[player], я хочу тебе кое-что сказать."
    show sayori at t11 zorder 4
    mc "Да?"
    show sayori 1bd at t11 zorder 4
    window hide
    pause (2.0)
    show sayori 1bzc at f11 zorder 4
    play music t9
    s "Я просто хотела поблагодарить тебя за то, что ты заботишься обо мне."
    s "Как ты спас меня, когда я видела самоубийство как единственный выход..."
    s "О том, как ты защищаешь меня и заставляешь меня чувствовать себя в безопасности."
    s 2bzd "Я тебе очень благодарна, очень..."
    show sayori 2bt at t11 zorder 4
    mc "Я тоже благодарен тебе, [persistent.sayoriname]."
    mc "Ты не считаешь меня каким-то монстром со сверхсилами."
    mc "То, как ты обращаешься со мной, заставляет меня чувствовать, что я не так уж сильно отличаюсь от всех вас."
    mc "Это... очень мило."
    scene bg black with dissolve_scene_full
    "Мы оба прослезились и обнимаем друг друга."
    "Просто мысль о том, что у нас не было бы такого момента без моих сил, вызывает во мне почти ненависть."
    "Я хочу сделать всё, что в моих силах, чтобы положить конец влиянию Моники раз и навсегда."
    "Даже если она осознала, что поступила неправильно, я никогда не могу быть уверен…"
    "Она всё ещё ревнует, и у неё всё ещё есть возможность изменить этот мир."
    "Если бы я только мог как-нибудь забрать её у неё..."
    scene bg living_room with dissolve_scene_full
    pause (1.0)
    show sayori 1by at f11 zorder 4
    s "..."
    s "[player], я хочу, чтобы мы остались вместе навсегда."
    s "Я знаю, что это эгоистичная мысль,{w=0.5}, но- {nw}"
    show sayori 3be at t11 zorder 4
    "Я осторожно беру её за руку."
    mc "[persistent.sayoriname]... У меня не было бы другого выхода, понимаешь?"
    mc "И если это возможно{w=0.25}.{w=0.25}.{w=0.25}. то однажды я смогу взять тебя в свой мир."
    mc "Но где бы мы ни были, я хочу быть с тобой."
    show sayori at f11 zorder 4
    s "Ты..."
    s "Ты бы сделал это?"
    show sayori at t11 zorder 4
    mc "Конечно! Возможно, так будет лучше..."
    mc "Как бы то ни было, я уверен, что однажды мы все сможем туда переехать."
    mc "Но, кажется, я забыл сказать тебе кое-что очень важное."
    show sayori 1bb at f11 zorder 4
    s "А?"
    show sayori at t11 zorder 4
    mc "Этот мир, в котором ты живёшь... это на самом деле видеоигра в моём мире."
    show sayori 2bh at f11 zorder 4
    s "Ч-что?"
    s "Мой мир... это видеоигра?"
    s 4bw "Значит ли это, что я не настоящая?!"
    show sayori at t11 zorder 4
    mc "Нет! Нет!"
    mc "Ты настоящая!"
    show sayori 1bv at t11 zorder 4
    mc "Все здесь настоящие, поэтому этот мир гораздо больше, чем просто игра."
    mc "Вы не работаете по какому-то сценарию, у вас есть настоящие чувства."
    mc "Никто не может этого отрицать."
    show sayori 1bzd at f11 zorder 4
    s "Думаю, в этом ты прав."
    s 2bv "Мне было бы очень больно знать, что я не настоящий человек."
    show sayori at t11 zorder 4
    mc "Это понятно, даже я бы счёл это тревожным."
    mc "Но тебе не о чем беспокоиться."
    mc "Никто не может причинить нам вред или контролировать нас, я могу связать этот мир со своими желаниями своей волей."
    mc "И я никому не позволю манипулировать тобой или другими."
    show sayori 4bzd at f11 zorder 4
    s "Спасибо, [player]."
    show sayori 4bt at t11 zorder 4
    mc "Это меньшее, что я могу сделать, ха-ха."
    mc "Ещё кое-что..."
    show sayori 1bb at t11 zorder 4
    mc "Э-э... Мне действительно нужно было сказать тебе об этом раньше."
    mc "Но есть кто-то, у кого есть сила, способная изменить этот мир."
    show sayori 1bz at f11 zorder 4
    s "Ч-что?!"
    s 4bz "[player], как много ты забыл мне сказать?"
    show sayori at t11 zorder 4
    mc "Извини, мне никогда не удавалось найти на это время."
    show sayori 1bg at t11 zorder 4
    mc "А также возможно, что я забыл об этом заговорить..."
    mc "Есть ещё несколько вещей, которых ты не знаешь, но тебе не о чем беспокоиться."
    mc "Ничто не повредит тебе, я позабочусь об этом."
    show sayori 2bh at f11 zorder 4
    s "К-кто это?"
    show sayori 2bg at t11 zorder 4
    mc "Если бы я сказал тебе, всё стало бы намного сложнее, чем должно быть."
    mc "В конце концов ты узнаешь, не волнуйся."
    mc "Но тебе не нужно слишком много думать об этом, я намного сильнее их."
    show sayori 2bv at f11 zorder 4
    s "Почему кто-то хочет причинить нам вред?"
    show sayori at t11 zorder 4
    mc "Есть много причин, по которым человек хочет заставить других страдать."
    mc "Тебе даже не нужно ничего делать кому-то, чтобы они тебя ненавидели."
    mc "Что касается того, о котором я говорю..."
    mc "Я знаю, что он не злой, и я знаю, что могу ему помочь."
    show sayori 2bh at f11 zorder 4
    s "Хорошо..."
    s 1bh "Но если тебе когда-нибудь понадобится моя помощь, просто скажи."
    show sayori 1bg at t11 zorder 4
    mc "Я буду иметь это в виду."
    show sayori 1bd at t11 zorder 4
    mc "Я просто хотел, чтобы ты знала, что ты в безопасности от его влияния."
    show sayori 1bc at f11 zorder 4
    s "Все остальные тоже в безопасности?"
    show sayori 1bb at t11 zorder 4
    mc "Да, их силы зависят от... консоли, можно сказать?"
    mc "Я могу предотвратить их использование в любое время, когда захочу."
    mc "И я знаю, что когда он пытается с этим возиться, я это ясно вижу."
    mc "Любая его попытка будет совершенно бессмысленной."
    show sayori 2bzc at f11 zorder 4
    s "Знать, это меня успокаивает."
    s 1bh "Но тебе стоило сказать мне об этом раньше..."
    show sayori 1bg at t11 zorder 4
    mc "Я знаю, я знаю."
    mc "Но я думаю, это нормально после того, как им пришлось бороться с его попытками контроля."
    mc "Сейчас я пойду к Монике за бумагами."
    mc "Ты останешься здесь?"
    show sayori 2bx at f11 zorder 4
    s "Да, я буду ждать тебя."
    show sayori 4ba at t11 zorder 4
    mc "В таком случае, я скоро вернусь."
    mc "Увидимся позже! Люблю тебя!"
    show sayori 1bzc at f11 zorder 4
    s "Я тебя тоже люблю!"
    scene bg black with dissolve_scene_full
    "Я прощаюсь и направляюсь прямо к дому Моники."
    window hide
    pause (1.0)
    scene bg house2 with dissolve_scene_full
    "Я звоню ей в дверь."
    "..."
    "Она подходит к дверям."
    show monika 2bd at t11 zorder 4
    window hide
    pause(1.6)
    show monika 1bb at f11 zorder 4
    m "Привет, [player]!"
    show monika 1ba at t11 zorder 4
    mc "Привет!"
    mc "Я здесь для работы, которую ты должна выполнить."
    show monika 2bn at f11 zorder 4
    m "Я забыла взять её с собой."
    m 2bb "Дайте мне секунду, пожалуйста."
    show monika at thide zorder 4
    hide monika
    "Она уходит за бумагами."
    "Приятно видеть, что ей становится лучше."
    "Ну… по крайней мере, на первый взгляд."
    "Я не могу знать, что она на самом деле чувствует, поэтому пока что я должен доверять ей."
    show monika 3bb at f11 zorder 4
    m "Вот."
    show monika 1ba at t11 zorder 4
    "Она протягивает мне бумаги."
    "К моему удивлению, их не так много, как я думал."
    mc "Отлично! Тогда я пойду."
    show monika 3bd at f11 zorder 4
    m "[player]! Подожди!"
    m "Я хотела тебя кое о чём спросить..."
    m 2bp "Игрок выбрал тебе имя до того, как ты пришёл, если я не ошибаюсь."
    m 2bd "И если это так, то [player] не твоё настоящее имя, не так ли?"
    if persistent.playername == "Барион" or persistent.playername == "Baryon":
        show monika 2bc at t11 zorder 4
        mc "Ты удивишься, но на самом деле это моё имя."
        mc "Но как он узнал, выше моего понимания..."
        mc "Будь уверена, всё, что он может делать, это просто смотреть, он не имеет никакого влияния."
        mc "Я даже могу позволить ему поговорить с нами."
        mc "Подожди..."
        "Я поднимаю руку, пытаясь использовать свою волю."
        window hide
        pause(1.5)
        show screen tear (25, 0,05, 0,05, -20, 80)
        play sound "sfx/glitch2.ogg"
        pause(0,6)
        hide screen tear
        menu:
            "Ты слышишь меня?":
                pass
        show monika 1bb at f11 zorder 4
        m "Ага! Громко и ясно."
        show monika 1ba at t11 zorder 4
        mc "Идеально."
        jump phase6
    
    if persistent.playername == "барион" or persistent.playername == "baryon":
        show monika 2bc at t11 zorder 4
        mc "Ты удивишься, но на самом деле это моё имя."
        mc "Но как он узнал, выше моего понимания..."
        mc "Будь уверена, всё, что он может делать, это просто смотреть, он не имеет никакого влияния."
        mc "Я даже могу позволить ему поговорить с нами."
        mc "Подожди..."
        "Я поднимаю руку, пытаясь использовать свою волю."
        window hide
        pause(1.5)
        show screen tear (25, 0,05, 0,05, -20, 80)
        play sound "sfx/glitch2.ogg"
        pause(0,6)
        hide screen tear
        menu:
            "Ты слышишь меня?":
                pass
        show monika 1bb at f11 zorder 4
        m "Ага! Громко и ясно."
        show monika 1ba at t11 zorder 4
        mc "Идеально."
        jump phase6
    
    show monika 2bc at t11 zorder 4
    mc "Ты права, но это не моё настоящее имя."
    show monika 1bd at f11 zorder 4
    m "Тогда какое твоё настоящее имя?"
    show monika 1bc at t11 zorder 4
    mc "Ты можешь звать меня Барион."
    mc "Вот кем я известен людям моего мира."
    mc "Подожди... позволь мне это изменить."
    mc "Надеюсь, остальным это не покажется слишком странным."
    mc "И если это так, я должен придумать что-нибудь быстро."
    window hide
    pause(1.5)
    $ player = "Барион"
    $ persistent.incorrect_name = True
    pause (1.0)
    mc "Ну вот, теперь намного лучше."
    jump phase6

label phase6:
    mc "Теперь, когда с этим разобрались..."
    mc "Я ухожу, и я полагаю, что мы увидимся завтра в школе."
    show monika 2bb at f11 zorder 4
    m "Ага, увидимся там!"
    scene bg residential_day with dissolve_scene_full
    stop music fadeout 3.0
    "Я поворачиваюсь и иду прямо назад."
    "Вдалеке я смог заметить кого-то знакомого."
    "Подожди{w=0.25}.{w=0.25}.{w=0.25}. Нацуки?"
    "Я бегу к ней."
    mc "Нацуки! Подожди!"
    show natsuki 2bd at f11 zorder 4
    play music t5
    n "О, привет, [player]!"
    show natsuki 4ba at t11 zorder 4
    mc "Эй!"
    if persistent.incorrect_name == True:
        "Кажется, она понятия не имеет, что моё имя изменилось в её памяти..."
        show natsuki 2bza at f11 zorder 4
        n "..."
        n 1bc "Подожди секунду... почему мне кажется, что я знаю тебя как кого-то другого?"
        show natsuki 1bza at t11 zorder 4
        "А может, и нет."
        mc "О чём ты говоришь?"
        mc "Ты всегда знала меня как [player]."
        "Прости за это, Нацуки."
        show natsuki 5bi at f11 zorder 4
        n "Хм..."
        n 5bq "Думаю, это просто я."
        n 1bc "В любом случае, что ты хочешь?"
    mc "Я хотел спросить тебя о том, что не давало мне покоя со вчерашнего дня."
    show natsuki 1bza at t11 zorder 4
    mc "Ты сказала, что было трудно убедить твоего отца позволить тебе прийти."
    mc "Почему это?"
    show natsuki 5br at f11 zorder 4
    n "Тьфу, я тоже этого не понимаю."
    n "Я должна идти куда захочу, не споря с ним!"
    n "Иногда достаточно просто сказать ему об этом."
    n 5bw "И особенно когда он пьян."
    n "Ему почти всё равно, когда он пьяный, и я могу сказать ему, что он позволил мне, если он начнёт жаловаться."
    show natsuki 5bx at t11 zorder 4
    mc "Нацуки... ты могла бы нам сказать об этом."
    show natsuki 1bu at f11 zorder 4
    n "Нет, всё в порядке."
    n 2bt "Просто забудь, я привыкла."
    show natsuki 2bs at t11 zorder 4
    mc "Мой друг сказал мне то же самое несколько лет назад."
    show natsuki 1bn at t11 zorder 4
    mc "Но я знал, что просто должен был помочь ему сопротивляться родительскому контролю."
    mc "Нацуки... ты должна постоять за себя."
    show natsuki 1bp at f11 zorder 4
    n "Ты что, шутишь?!"
    n "Он выбьет из меня всё дерьмо!!"
    show natsuki at t11 zorder 4
    mc "Нет, если я буду там, чтобы предотвратить это."
    show natsuki 1bm at f11 zorder 4
    n "..."
    n "Я не хочу рисковать тем, что ты пострадаешь из-за него."
    show natsuki 1bn at t11 zorder 4
    mc "Я не пострадаю, можешь на это рассчитывать."
    "Я больше беспокоюсь о том, чтобы случайно не ранить её отца…"
    mc "Но ты должна отстаивать свою позицию, и я знаю, что ты можешь это сделать."
    show natsuki 5bs at t11 zorder 4
    window hide
    pause (2.0)
    show natsuki 5bq at f11 zorder 4
    n "Ты прав, я должна перестать позволять ему так командовать мной."
    n 1bh "С меня довольно! Пойдём со мной!"
    show natsuki at t11 zorder 4
    "Она долго ждала этой возможности…"
    "Её типичная пренебрежительная личность полностью исчезла."
    "Это может быть или не быть подходящим моментом, когда я раскрою ей свои силы."
    "Тем не менее, она тоже должна знать об этом в какой-то момент."
    scene bg house3 with dissolve_scene_full
    "Мы подходим к передней части дома."
    "К моему удивлению, отец Нацуки уже на улице."
    show natsukidad 1b at f11 zorder 4
    nd "Нацуки?"
    show natsukidad 1k at t11 zorder 4
    "Он смотрит на меня, и выражение его лица почти мгновенно меняется."
    show natsukidad 4l at f11 zorder 4
    nd "Ты встречалась с мальчиком?!"
    show natsukidad 4m at t21 zorder 3
    show natsuki 1bzb at t22 zorder 4
    stop music fadeout 6.0
    "Я замечаю страх Нацуки в её глазах."
    "Найди это в себе, у тебя есть это..."
    window hide
    pause(1.5)
    show natsuki 1bx at t22 zorder 4
    pause (2.0)
    show natsuki 5be at f22 zorder 4
    n "Да, это так! Это проблема?"
    show natsuki 5bza at t22 zorder 3
    show natsukidad 1l at f21 zorder 4
    nd "Разве я не говорил тебе громко и ясно, чтобы ты не тусовалась с мальчиками?!"
    show natsukidad 1m at t21 zorder 3
    show natsuki 1bp at f22 zorder 4
    n "Почему?! Почему мне нельзя тусоваться с парнями?!"
    n "[player] не преступник!!"
    show natsuki 1bo at t22 zorder 3
    show natsukidad 3l at f21 zorder 4
    nd "Мне всё равно, кто он! Тебя больше не будет рядом с парнями!"
    show natsukidad 3m at t21 zorder 3
    show natsuki 5bh at f22 zorder 4
    n "Нет."
    show natsuki 5bi at t22 zorder 3
    show natsukidad 1l at f21 zorder 4
    nd "Что?!"
    show natsukidad 1k at t21 zorder 3
    show natsuki 5be at f22 zorder 4
    n "Я сказала нет!"
    n 1be "Не тебе указывать мне, с кем быть, а с кем не быть!"
    n 1bf "Я устала от того, что ты контролируешь мою жизнь!!"
    show natsukidad 1m at t21 zorder 3
    show natsuki at t22 zorder 4
    "Я был прав, полагая, что у неё есть силы, чтобы сделать это."
    "Она выпустила всё разочарование, и вот результат."
    "Это действительно напоминает мне о себе несколько лет назад."
    "Я горжусь тобой, Нацуки."
    show natsukidad 4l at f21 zorder 4
    nd "Ты хоть представляешь, сколько мне стоит содержать тебя?!"
    nd "Я кормлю тебя и позволяю тебе жить под моей крышей! Ты должна быть благодарна!"
    show natsukidad 4m at t21 zorder 3
    show natsuki 1bp at f22 zorder 4
    n "Ты? Кормишь меня?!"
    n "Ты едва даёшь мне достаточно! Из-за тебя мне пришлось научиться печь!"
    n "Мне пришлось перенести свою коллекцию манги в класс, потому что ты бы её выбросил!"
    show natsuki 1bo at t22 zorder 3
    show natsukidad 1l at f21 zorder 4
    nd "Ты {i}что{/i}?!"
    nd 1m "Всё, с меня хватит!"
    nd 3m "Я должен преподать тебе хороший урок, который ты никогда не забудешь."
    show natsukidad at t21 zorder 3
    show natsuki 1bzb at t33 zorder 4
    "Когда он собирался начать её бить, я встал перед Нацуки."
    show natsuki at thide zorder 4
    hide natsuki
    show natsukidad at t11 zorder 4
    mc "Всё в порядке, Нацуки."
    mc "Он не тронет тебя, я тебе это обещаю."
    show natsukidad 5l at f11 zorder 4
    nd "Это отец с тобой разговаривает! Ты себя кем возомнил?!"
    show natsukidad 5m at t11 zorder 3
    mc "А ТЫ себя кем возомнил?!"
    mc "Думаешь, это нормально – так бить свою дочь?!"
    mc "Она должна чувствовать себя в безопасности рядом с тобой! Но вместо этого она боится!"
    mc "Тебе не кажется, что так быть не должно?!"
    show natsukidad 1l at f11 zorder 4
    nd "Что ты знаешь обо мне?!"
    nd "Я дал ей всё, что она когда-либо хотела!"
    show natsukidad 1m at t11 zorder 4
    mc "И поэтому она должна держать свою коллекцию манги подальше от тебя?"
    show natsukidad 3l at f11 zorder 4
    nd "Она должна вырасти из этого! Ей 18!"
    show natsukidad 3k at t11 zorder 4
    mc "Ну и что? Это не значит, что она должна отказаться от того, что ей нравится делать."
    mc "Это её решение, и как её отец, ты должен уважать его!"
    show natsukidad 1m at f11 zorder 4
    nd "..."
    nd 3m "Ты тоже хочешь, чтобы тебя избили?!"
    show natsukidad at t11 zorder 4
    menu:
        " "
        "Стать агрессивным":
            $ value = 14
            $ persistent.brutality = True
        "Защититься":
            $ value = 15
    if value == 14:
        pause (2.0)
        play sound "sfx/fire2.ogg"
        show natsukidad 1x в h11 zorder 4
        pause (1.0)
        mc "Н{w=0.05}у{w=0.05} ж{w=0.05}е{w=0.05}."
        mc "Т{w=0.05}о{w=0.05}л{w=0.05}ь{w=0.05}к{w=0.05}о{w=0.05} п{w=0.05}о{w=0.05}п{w=0.05}р{w=0.05}о{w=0.05}б{w=0.05}у{w=0.05}й."
        show natsukidad 1y at t11 zorder 4
        "Страх пронзает его глаза, и он становится не в состоянии обработать то, что он сейчас видит."
        show natsukidad 2x at f11 zorder 4
        nd "Ч-что такое?!.."
        show natsukidad 2y at t21 zorder 3
        show natsuki 1bp at f22 zorder 4
        n "[player]?! Что с тобой происходит?!"
        show natsuki at t22 zorder 4
        mc "Не волнуйся, мне это не больно."
        show natsuki at thide zorder 4
        hide natsuki
        show natsukidad at t11 zorder 4
        mc "Нацуки не та, кто должен учить урок."
        mc "Ты должен пересмотреть свое отношение к ней."
        mc "Всё, что ей нужно, это отец, который поддерживает её, а ты даже этого не можешь сделать?!"
        mc "Что она сделала с тобой, что заставило тебя сделать это?!"
        jump phase7
    
    if value == 15:
        pause (2.0)
        mc "Я тебя не боюсь."
        scene bg black with dissolve_scene_full
        "Он бросается на меня и наносит удар."
        "Почти без усилий я отразил удар и ударил его в ответ, заставив его упасть на землю."
        "Мои глаза начинают слегка светиться от высвобождения моей силы."
        mc "Нацуки не та, кто должен учить урок."
        mc "Ты должен пересмотреть свое отношение к ней."
        mc "Все, что ей нужно, это отец, который поддерживает её, а ты даже этого не можешь сделать?!"
        mc "Что она сделала с тобой, что заставило тебя сделать это?!"
        scene bg house3 with dissolve_scene_full
        pause (1.0)
        jump phase7

label phase7:
    show natsukidad 1x at f11 zorder 4
    nd "Я..."
    show natsukidad 1s at t11 zorder 4
    window hide
    pause(1.5)
    show natsukidad 1t at s11 zorder 4
    pause(1.5)
    play music mend
    nd 1u "Ты прав..."
    nd "Всё это время я ужасно с ней обращался."
    show natsukidad 1v at t21 zorder 3
    show natsuki 1bp at f22 zorder 4
    n "Ты только сейчас это понял?!"
    n 1bo "Ты годами бил меня и делал мои дни невыносимыми!"
    n "И ты понимаешь это только после того, как [player] сказал тебе то, что я пыталась сказать тебе всё это время?!"
    show natsuki at t22 zorder 3
    show natsukidad 4r at f21 zorder 4
    nd "Прости, Нацуки! Я был не прав..."
    nd 4s "Ты имеешь полное право злиться на меня."
    nd 4t "..."
    nd 1r "Нацуки, тебе больше не нужно прятать свою мангу."
    show natsuki 1bc at t22 zorder 3
    nd "Я ужасный отец, потому что не понимаю, как ты к этому относишься…"
    nd "Отныне общайся с кем хочешь, я не буду говорить тебе, что делать."
    show natsuki 2bm at f22 zorder 4
    show natsukidad 1q at t21 zorder 3
    n "Ты{w=0.25}.{w=0.25}.{w=0.25}. серьёзно?"
    show natsuki at t22 zorder 3
    show natsukidad 1r at f21 zorder 4
    nd "Естественно."
    nd "Иди делай, что хочешь, меня не должно быть рядом с тобой..."
    show natsukidad 1q at t21 zorder 3
    show natsuki 1bm at f22 zorder 4
    n "Папа..."
    n "Это не то, чего я хочу."
    n "Я вступила в Литературный клуб, потому что хотела чувствовать себя в безопасности."
    n "И я встретила новых друзей."
    n "Я чувствую себя в безопасности рядом с ними, это как дом, которого у меня никогда не было."
    n "Дом, где я могла бы быть самой собой, где я могла бы поделиться своими увлечениями и интересами."
    show natsuki 1bn at t22 zorder 3
    show natsukidad 1r at f21 zorder 4
    nd "И наш дом – это место, где ты чувствуешь себя неуверенно и под угрозой."
    nd "Я должен был больше слушать тебя, мне очень жаль…"
    show natsukidad 1q at t21 zorder 3
    show natsuki 1bm at f22 zorder 4
    n "Папа, я знаю, что развод плохо на тебя повлиял."
    n "Мне тоже было не по себе, поверь мне."
    n "Но у тебя всё ещё есть я, и ты не должен об этом забывать."
    show natsuki 1bn at t22 zorder 3
    mc "Правильно, Нацуки всё ещё здесь для тебя."
    mc "Вы двое должны поддерживать друг друга в трудные времена."
    mc "Так вам обоим будет лучше и удобнее."
    show natsukidad 2o at f21 zorder 4
    nd "[player]?.."
    nd 1o "Я извиняюсь за то, как я себя вёл, это было действительно незрело с моей стороны."
    show natsukidad 1n at t21 zorder 4
    mc "По крайней мере, у тебя есть саморефлексия."
    mc "Я прощаю тебя, но прощение Нацуки должно быть для тебя важнее сейчас."
    show natsukidad 3o at f21 zorder 4
    nd "Нацуки..."
    show natsukidad 3n at t21 zorder 3
    show natsuki 5bt at f22 zorder 4
    n "Да, я прощаю тебя."
    n 5bc "Но больше не бить меня!"
    show natsuki at t22 zorder 3
    show natsukidad 1o at f21 zorder 4
    nd "Я обещаю."
    show natsukidad 1n at t21 zorder 4
    "Думаю, это ещё одно дело раскрыто."
    "Всё прошло довольно гладко, почти слишком хорошо, чтобы быть правдой."
    "Но опять же, у него не было другого выхода..."
    "Может быть, будет лучше, если они помирятся, а не то, что я имел в виду."
    stop music fadeout 2.5
    scene bg black with dissolve_scene_full
    "Они продолжили разговор, и я отправился обратно к [persistent.sayoriname]."
    scene bg residential_day with dissolve_scene_full
    pause (1.0)
    n "[player]! Подожди меня!"
    show natsuki 4ba at t11 zorder 4
    play music t8
    mc "Ах, привет."
    mc "Полагаю, всё прошло хорошо?"
    show natsuki 5bz at f11 zorder 4
    n "Ага!"
    n 5bt "Я, э-э-э...{w=0.6} {nw}"
    extend 1bt "Я хотела поблагодарить тебя за то, что тогда ты дал мне мужество."
    show natsuki at t11 zorder 4
    mc "Всегда пожалуйста."
    mc "Я просто рад, что тебе больше не нужно бояться дома."
    show natsuki 2bc at f11 zorder 4
    n "Я до сих пор не уверена, серьёзно он говорил или нет."
    n 1bk "Но я хотела спросить тебя кое о чём."
    if value == 14:
        n "Это мне показалось, или у тебя на руках был огонь?"
        show natsuki 1bza at t11 zorder 4
        mc "Это будет очень трудно тебе объяснить."
        mc "Но да, я сформировал огонь в своих руках, пытаясь вселить страх в твоего отца."
        show natsuki 5bc at f11 zorder 4
        n "Как это вообще возможно?"
        n "Разве это не должно причинить тебе боль?"
        show natsuki at t11 zorder 4
        mc "Не буду стесняться в словах по этому поводу, и перейду сразу к делу..."
        mc "Дело в том, что я могу манипулировать огнём, а это значит, я ещё и огнестойкий."
        show natsuki 1bp at f11 zorder 4
        n "Ч-ЧТО?!"
        n "Ты что, шутишь?!"
        show natsuki at t11 zorder 4
        mc "На самом деле нет."
        mc "Всё это может показаться тебе безумием, или, может быть, у тебя всё ещё есть свои предположения на этот счет."
        mc "Но это моя сила, и это лишь одна из многих вещей, которые я могу сделать."
        show natsuki 1bo at f11 zorder 4
        n "..."
        n "Одна из многих вещей, которые ты можешь сделать?!"
        jump phase8

    if value == 15:
        n "Ты чуть не отправил моего отца в полёт, когда сражался с ним."
        n "Почему ты такой сильный? Такое ощущение, что ты обладаешь сверхчеловеческой силой."
        show natsuki 1bza at t11 zorder 4
        mc "На самом деле, ты совсем не ошибаешься."
        show natsuki 5bc at f11 zorder 4
        n "Что ты имеешь в виду?"
        show natsuki at t11 zorder 4
        mc "Я не собираюсь затягивать с этим, и перейду сразу к делу..."
        mc "Знаешь... У меня действительно есть сверхчеловеческая сила."
        show natsuki 1bp at f11 zorder 4
        n "Ч-ЧТО?!"
        n "Ты издеваешься надо мной?!"
        show natsuki at t11 zorder 4
        mc "Нет, не издеваюсь."
        mc "И это не единственное, что у меня есть."
        show natsuki 1bo at f11 zorder 4
        n "..."
        n "Не единственное, что у тебя есть?!"
        jump phase8

label phase8:
    show natsuki at t11 zorder 4
    "Я должен был догадаться, что у Нацуки будет самая острая реакция."
    mc "Успокойся, Нацуки."
    mc "Я хочу тебе всё объяснить, но перед этим мне нужно, чтобы ты очистила свой разум."
    show natsuki 1br at t11 zorder 4
    window hide
    pause (1.0)
    scene bg residential_day with dissolve_scene_full
    pause (1.0)
    show natsuki 2bq at f11 zorder 4
    n "Хорошо... Думаю, теперь я в порядке."
    show natsuki at t11 zorder 4
    mc "Ловлю на слове."
    show natsuki 2bza at t11 zorder 4
    mc "Ну, вот моя история..."
    scene bg black with dissolve_scene_full
    "Я объясняю ей, что я пришёл из другого мира, и что я обладаю сверхъестественными способностями."
    "Кроме того, я рассказываю ей о том, как я знал, что происходит в отношениях между ней и её отцом."
    scene bg residential_day with dissolve_scene_full
    show natsuki 5bm at f11 zorder 4
    n "[player], поэтому ты предложил мне жить в твоём доме?"
    show natsuki 5bn at t11 zorder 4
    mc "Именно так."
    show natsuki 5bs at f11 zorder 4
    n "..."
    n 5bq "Теперь я чувствую себя ублюдочной из-за того, как иногда поступала с тобой."
    show natsuki 5bs at t11 zorder 4
    mc "Я действительно не против."
    mc "Это просто было неправильно, ты не заслуживаешь того, чтобы с тобой такое случалось."
    show natsuki 2bt at f11 zorder 4
    n "По крайней мере, теперь я понимаю, почему ты сказал мне, что не пострадаешь."
    n 1bq "И если честно... Я бы солгала, если бы сказала, что сейчас я совсем не боюсь."
    show natsuki 1bs at t11 zorder 4
    mc "Тебе не нужно бояться, я не собираюсь причинять тебе вред."
    mc "Наоборот, я бы не сделал всего этого, если бы ты захотела, не так ли?"
    show natsuki 1bt at f11 zorder 4
    n "Думаю, ты прав."
    n 2bc "А я думала, что сверхъестественные силы не существуют..."
    show natsuki at t11 zorder 4
    mc "Может быть, они не настоящие в вашем мире, кто знает?"
    mc "И нет, я не всезнающий, прежде чем ты спросишь об этом."
    show natsuki 5bd at f11 zorder 4
    n "Это большое облегчение."
    n 5bq "Без обид, мне просто было бы неудобно, если бы ты знал обо мне всё."
    show natsuki 5bs at t11 zorder 4
    mc "Я понимаю, меня бы это тоже сильно беспокоило."
    show natsuki 1bc at f11 zorder 4
    n "Ещё один вопрос, о котором я хочу тебя спросить."
    n 1bt "Ну... я не могу обещать тебе, что это последний вопрос."
    n 1bk "Но, знают ли другие девушки о твоих{w=0.25}.{w=0.25}.{w=0.25}. потусторонних силах?"
    show natsuki 1bza at t11 zorder 4
    mc "Извини, но я не могу об этом говорить."
    show natsuki 1bm at f11 zorder 4
    n "О, хорошо..."
    n "Я понимаю."
    n 5bt "Ну, всё, на что я могу сейчас надеяться, это то, что я не увижу мир в огне и руинах, когда проснусь завтра."
    n "Ну или скорее... ЕСЛИ я проснусь завтра."
    show natsuki at t11 zorder 4
    mc "Ха-ха, тебе действительно не о чем беспокоиться."
    show natsuki at f11 zorder 4
    n "Надеюсь."
    n 1bk "Но мне кое-что интересно."
    n "Должна быть другая причина, по которой ты пришёл сюда, кроме помощи мне, верно?"
    show natsuki 1bza at t11 zorder 4
    mc "Действительно..."
    mc "На самом деле, тому есть несколько причин."
    mc "Я не буду вдаваться в подробности, но можно с уверенностью сказать, что ими не следует пренебрегать."
    mc "Особенно та, которая..."
    "Я останавливаю себя перед тем, как случайно выдать то, что Моника хотела сделать с ними."
    mc "Неважно, мне пора возвращаться."
    mc "Я сказал [persistent.sayoriname], что принесу всю работу от Моники, а меня уже давно нет."
    mc "Увидимся завтра на собрании клуба!"
    show natsuki 2bd at f11 zorder 4
    n "Да, увидимся завтра!"
    scene bg house with dissolve_scene_full
    "Я прихожу к дому [persistent.sayoriname], всё ещё думая о том, что теперь все девушки знают о моих силах."
    "Тем не менее, только Юри и [persistent.sayoriname] знают, что, кроме них, есть ещё один, кто разделяет эти знания."
    "Думаю, могло быть и хуже…"
    scene bg living_room with dissolve_scene_full
    pause (1.0)
    mc "[persistent.sayoriname]! Я вернулся!"
    show sayori 4br at f11 zorder 4
    s "[player]!"
    show sayori 4bs at t11 zorder 4
    "Я притягиваю её к себе и целую в щёку."
    mc "Извини, что так долго, я был занят разговором с Нацуки на обратном пути."
    show sayori 2bzc at f11 zorder 4
    s "Я уже начала немного волноваться, что что-то случилось."
    if persistent.incorrect_name == True:
        s 1bb "..."
        s 1bc "Почему у меня такое чувство, что [player] – это не твоё настоящее имя?"
        s 1bl "Я знаю, это звучит странно, но..."
        show sayori at t11 zorder 4
        mc "Позволь мне объяснить тебе..."
        show sayori 1bb at t11 zorder 4
        mc "Тот, кем ты знала меня раньше, это не было моим настоящим именем."
        mc "Это имя дал мне кто-то другой."
        mc "И так как у меня были более важные дела, о которых нужно было позаботиться, я просто оставил всё как есть."
        mc "Вплоть до момента, когда я изменил его, в результате чего у всех, кто разговаривал со мной, была заменена память."
        show sayori 1bl at f11 zorder 4
        s "Знаешь... меня больше ничего не удивляет."
        s 2bh "Но как я могла сразу не заметить?"
        show sayori 2bg at t11 zorder 4
        mc "Это что-то за пределами моего понимания..."
        show sayori 1bl at f11 zorder 4
        s "О... хорошо."
    s 1bc "Пока я не забыла, бумаги у тебя?"
    show sayori 1bb at t11 zorder 4
    mc "Конечно."
    show sayori 1ba at t11 zorder 4
    mc "Мы сразу приступим к ним?"
    show sayori 1bx at f11 zorder 4
    s "Мы могли бы, тогда нам не придется беспокоиться об этом позже!"
    show sayori 1ba at t11 zorder 4
    mc "По-моему, неплохо!"
    scene bg black with dissolve_scene_full
    "Мы начинаем работать над бумагами, и как только мы закончим, мы оба идём и возвращаем их Монике."
    "После этого мы вместе смотрим сериалы и играем в игры."
    stop music fadeout 3.0
    "Внезапно [persistent.sayoriname] спрашивает меня, можем ли мы выйти на улицу и поговорить о чём-нибудь."
    "Я киваю в знак согласия, и мы выходим на улицу."
    scene bg housenight with dissolve_scene_full
    "[persistent.sayoriname] и я вместе сидим перед воротами."
    show sayori 1by at t11 zorder 4
    play music t9
    mc "Прекрасный вид, не правда ли?"
    show sayori 1bl at f11 zorder 4
    s "Да..."
    s 1bh "[player], я давно об этом думала."
    s 2bh "Как ты думаешь, мне стоит пойти на психотерапию?"
    show sayori 2bg at t11 zorder 4
    "Я делаю глубокий вдох, прежде чем начать говорить."
    mc "Это всё зависит от тебя, я бы не хотел заставлять тебя это делать, если ты не чувствуешь себя комфортно."
    mc "Но я думал об этом, и я мог бы быть там с тобой."
    show sayori 1bv at f11 zorder 4
    s "Ты действительно сделаешь это для меня?"
    show sayori at t11 zorder 4
    mc "[persistent.sayoriname]... Я хочу, чтобы ты была счастлива, это так же важно для меня, как моё счастье важно для тебя."
    show sayori 4bt at f11 zorder 4
    s "..."
    show sayori at thide zorder 4
    hide sayori
    "Не говоря больше ни слова, она обнимает меня и начинает рыдать."
    "Но это слёзы счастья, слёзы облегчения."
    "Прошло достаточно много времени, чтобы я смог это различить."
    mc "Я бы с удовольствием пошел туда с тобой, пока ты не найдёшь в себе силы пойти туда самостоятельно."
    mc "И это нормально, если это займёт у тебя много времени. Если это поможет, вот что важно."
    show sayori 4bzd at f11 zorder 4
    s "[player]..."
    s "Это так много значит для меня."
    s 1bv "Было так трудно бороться с серыми тучками, пока я была одна."
    s "Я потеряла всякую надежду и подумала, что не смогу быть счастливой с тобой."
    s 2bzd "Но, несмотря на это, ты не переставал пытаться."
    s "Ты продолжал идти за мной, даже когда я пыталась скрыть от тебя свои чувства."
    show sayori 2bt at t11 zorder 4
    mc "Я не мог просто стоять и ничего не делать."
    mc "Внутри тебе было больно, но ты все равно пыталась сделать всех вокруг счастливыми."
    mc "Так долго носить такую маску... ты действительно сильная, [persistent.sayoriname]."
    show sayori 1by at f11 zorder 4
    s "..."
    s 1bl "[player], я не настолько сильная."
    show sayori 1by at t11 zorder 4
    mc "Нет, ты сильная."
    show sayori 1be at t11 zorder 4
    mc "Поверь мне, я знаю, о чём говорю."
    mc "Ты потрясающая, [persistent.sayoriname]."
    mc "Никогда не забывай, я люблю тебя такой, какая ты есть."
    show sayori 3bt at t11 zorder 4
    mc "То, что я был с тобой, показало мне, что ты искренне заботишься обо мне."
    mc "Мне было достаточно видеть это по мельчайшим деталям."
    mc "И я слишком забочусь о тебе, чтобы позволять какой-то депрессии беспокоить тебя весь день."
    "Кроме того, я очень рад, что смог помочь ей..."
    show sayori 3bzc at f11 zorder 4
    s "[player]..."
    s "Ничего, если мы побудем здесь вместе ещё немного?"
    show sayori 3bd at t11 zorder 4
    mc "Абсолютно."
    scene bg black with dissolve_scene_full
    "Мы продолжаем смотреть на звёзды в тишине, оба ценя тот факт, что мы есть друг у друга."
    "Некоторое время спустя, не спрашивая и не колеблясь, мы снова ложимся спать вместе."
    "Полагаю, что моя комната сейчас будет в основном неиспользуемой."
    "Но мне всё равно, так намного лучше..."
    stop music fadeout 2.5
    scene bg sayori_bedroom with dissolve_scene_full
    pause (1.0)
    "Сейчас раннее утро, а я уже просыпаюсь."
    "Я полагаю, что в том, чтобы ложиться спать раньше, есть свои преимущества."
    show sayori 2px at f11 zorder 4
    play music t2
    s "Привет, [player]!"
    show sayori 2pa at t11 zorder 4
    mc "Привет!"
    mc "С нетерпением жду встречи клуба снова."
    mc "Но я надеюсь, что Юри в порядке, мы не видели её с субботы..."
    show sayori 1ph at f11 zorder 4
    s "Бедная девочка чувствует себя одинокой, не так ли?"
    show sayori 1pg at t11 zorder 4
    mc "Предположительно, но я действительно мало знаю о её повседневной жизни, поэтому не могу сказать."
    mc "Мы могли бы взять её куда-нибудь после школы, я думаю, она была бы признательна..."
    show sayori 4px at f11 zorder 4
    s "Мне кажется, это хорошая идея!"
    s 2pc "Но куда мы могли её взять?"
    show sayori 2pb at t11 zorder 4
    mc "Хе-хе... кроме нескольких мест, я понятия не имею, где что находится."
    show sayori 1pl at f11 zorder 4
    s "О, верно."
    s "Так легко забыть, что весь этот город на самом деле для тебя новый."
    s 2pc "Разве ты не можешь использовать свои силы, чтобы как-то узнать, где что находится?"
    show sayori 2pb at t11 zorder 4
    mc "Это работает только с людьми, с которыми я разговаривал хотя бы раз."
    mc "Если я хочу знать, где что-то находится, я должен туда добраться, тогда я смогу вспомнить это в любой момент, когда захочу."
    show sayori 1pc at f11 zorder 4
    s "Ладно..."
    s 2pr "Но я уверена, что мы сможем что-нибудь придумать."
    show sayori 2pq at t11 zorder 4
    mc "Возможно, у Юри есть место, куда она хочет пойти."
    show sayori 1pa at t11 zorder 4
    mc "Меня устраивает всё, кроме любых... формальных мест, если можно так выразиться."
    show sayori 2pc at f11 zorder 4
    s "Формальные места? Почему это?"
    show sayori 2pb at t11 zorder 4
    mc "Просто мне это не нравится."
    mc "На самом деле больше нет причин."
    show sayori 1pzc at f11 zorder 4
    s "Всё в порядке, я уверена, что Юри поймёт."
    show sayori 1pd at t11 zorder 4
    mc "Она очень понимающий человек, это замечательно."
    mc "Большинство людей даже не пытаются."
    show sayori 4pj at f11 zorder 4
    s "Такие люди просто подлецы!"
    show sayori 4pi at t11 zorder 4
    mc "Я согласен с этим."
    mc "К сожалению, это обычная проблема в моем мире."
    show sayori 1pg at t11 zorder 4
    mc "Большинство людей там слишком осуждающие и требовательные."
    mc "Часть из-за того, что однажды я наполнился ненавистью, если ты помнишь, как мы говорили об этом."
    mc "Это заставляет меня ценить Литературный клуб."
    mc "И быть с тобой."
    show sayori 3pd at f11 zorder 4
    s "..."
    s 1pzc "Да, я тоже ценю то, что мы есть друг у друга."
    s 1pc "Но между нами не всегда было так, понимаешь?"
    show sayori 1pb at t11 zorder 4
    mc "Если подумать... Я действительно ничего не знаю о том, что произошло до того дня, когда ты познакомила меня с Литературным клубом."
    mc "Так как это было раньше?"
    show sayori 1ph at f11 zorder 4
    s "Мы часто ссорились, в основном Нацуки и Моника."
    s "Нам было трудно заслужить доверие и уважение друг друга."
    s 2pzc "Но мы выросли и узнали друг друга больше, и наши дела стали налаживаться."
    s 2pc "Конечно, иногда мы спорим, но это нормально."
    show sayori 2pb at t11 zorder 4
    mc "Наши различия делают нас уникальными."
    mc "Если бы мы все были одинаковыми, тогда не было бы смысла разговаривать друг с другом."
    show sayori 1px at f11 zorder 4
    s "Ага!"
    s 1pl "Ой, нам пора идти, скоро в школу."
    s 2px "А мы ещё должны позавтракать, прежде чем идти!"
    show sayori 2pa at t11 zorder 4
    mc "Меня не удивляет, что это первое, что ты не забываешь сделать перед выходом."
    scene bg black with dissolve_scene_full
    "После завершения утренней рутины мы идем в школу и терпим долгие часы."
    "Я заметил, что сегодняшнее расписание сокращено из-за фестиваля."
    "Правильно! Я совсем забыл об этом..."
    scene bg corridor with dissolve_scene_full
    mc "Надеюсь, мы не опоздали."
    show sayori 1x at f11 zorder 4
    s "Мы должны быть вовремя!"
    show sayori 1а at t11 zorder 4
    mc "Не могу проверить, я оставил свой телефон в своей комнате."
    mc "В любом случае, не будем больше терять время."
    scene bg club_day с dissolve_scene_full
    "Когда мы заходим в комнату, мы начинаем слышать спор между Моникой и Нацуки."
    stop music fadeout 15.0
    show monika 1f at t21 zorder 3
    show natsuki 5e at f22 zorder 4
    n "И ты даже не сказала нам об этом?!"
    n 1e "Что, если бы мы хотели что-то спланировать?!"
    show monika at t32 zorder 2
    show sayori 2h at f31 zorder 4
    show natsuki 1f at t33 zorder 3
    s "Ребята? Что происходит?"
    show sayori 2g at t41 zorder 3
    show monika at t42 zorder 2
    show natsuki at t43 zorder 4
    show yuri 4b at t44 zorder 1
    "Мы прибыли последними, так что Юри должна знать, что произошло между ними двумя."
    "Однако она отворачивается, давая мне знак, что не хочет об этом говорить."
    show natsuki 5e at f43 zorder 4
    n "По всей видимости, Моника «забыла» рассказать нам о подготовке к фестивалю."
    n "Они были созданы специально для клубов, чтобы продемонстрировать то, что они предлагают!"
    n "Мы могли бы что-нибудь организовать!"
    show natsuki 5f at t43 zorder 3
    show monika 1g at f42 zorder 4
    m "Послушай, я сожалею об этом."
    m "У меня было много работы, и это было нелегко."
    show monika 1f at t42 zorder 4
    show natsuki 1w at f43 zorder 4
    n "Это тебя не оправдывает!"
    n 1e "Ты президент клуба, ты должна помнить о таких важных событиях!"
    show sayori at thide zorder 4
    hide sayori
    show yuri at thide zorder 4
    hide yuri
    show natsuki 1g at t22 zorder 3
    show monika 1i at f21 zorder 4
    m "Нацуки, успокойся."
    m "Ты не знаешь, каково быть президентом."
    show monika 1h at t21 zorder 3
    show natsuki 2e at f22 zorder 4
    n "Ну, я бы точно справилась лучше, чем ты!"
    n 4f "Ты могла бы просто рассказать нам об этом!"
    n "Поскольку у тебя так много работы, мы могли бы подготовиться к фестивалю сами."
    n "Но ты даже этого не могла сделать?!"
    show natsuki at t22 zorder 3
    show monika 2i at f21 zorder 4
    m "Я попала в ситуацию, которую ты, вероятно, даже не можешь понять."
    m "И ты понятия не имеешь, каково это для меня."
    show monika 2h at t21 zorder 3
    show natsuki 5e at f22 zorder 4
    n "Ты думаешь, что ты единственная, у кого трудная жизнь?!"
    n "То, что мы не президенты клубов, не означает, что нам легко!"
    n 5w "Что ты вообще можешь понять, мисс совершенство."
    show natsuki 5x at t22 zorder 4
    "Чем больше я слушаю их спор, тем больше расстраиваюсь."
    "Чувство гнева и печали начинает завладевать моими мыслями."
    window hide
    pause(2.5)
    mc "ДОВОЛЬНО!!{w=0.1}{nw}"
    show natsuki 1p at h22 zorder 3
    show monika 1s at h21 zorder 4
    play sound "sfx/mscare.ogg"
    pause(0.1)
    show screen tear (30, 0.05, 0.05, -20, 80)
    hide screen tear
    show screen invert (1.5, 0.01)
    pause (1.0)
    play sound "sfx/glitch1.ogg"
    show screen tear (30, 0.05, 0.05, -20, 80)
    hide screen tear
    pause(1.0)
    hide screen invert
    pause(3.0)
    "Со всей силой моего разочарования, всё это место выглядело так, как будто оно готово разорваться на части."
    mc "Почему мы все просто не сможем поладить друг с другом?!"
    mc "Почему мы должны вот так спорить?! Почему это вообще что-то значит?!"
    mc "Мы здесь, чтобы понимать друг друга и помогать друг другу! В этом и есть весь смысл Литературного клуба!"
    mc "Конечно, Моника могла бы и рассказать всем об этом, но значит ли это теперь, что мы все набросимся на неё с обвинениями по этому поводу?!"
    mc "Вы вообще когда-нибудь задумывались о том, что вообще сейчас между нами?"
    mc "У нас есть доверие, мы так-то все друзья! Неужели нам нужно привлекать новых членов таким образом, чтобы старые отворачивались друг от друга?"
    mc "Я просто{w=0.25}.{w=0.25}.{w=0.25}. Я просто не хочу ссориться вот так..."
    show natsuki 1n at t22 zorder 3
    show monika 1g at t21 zorder 4
    "Я заканчиваю свой монолог. Эмоции постепенно ослабевают."
    "[persistent.sayoriname] подходит и обнимает меня, пытаясь утихомирить меня."
    show natsuki at t32 zorder 2
    show monika at t31 zorder 3
    show yuri 2r at f33 zorder 4
    y "[player] прав!"
    y "Как мы вообще можем надеяться на то, чтобы найти новых членов клуба, если мы даже друг с другом не можем поладить?"
    show yuri at t33 zorder 4
    "Наши глаза падают на Юри, и, кажется, она это заметила."
    show yuri 3n at f33 zorder 4
    y "Ах!"
    y 4b "И-извините, я не хотела так кричать."
    show yuri at t33 zorder 4
    mc "Нет... Всё в порядке, продолжай."
    show yuri 3w at t33 zorder 4
    "Юри делает глубокий вздох и продолжила там, где остановилась."
    show yuri 1t at f33 zorder 4
    y "Вы помните тот первый раз, когда я пришла в клуб? Я была необычайно стеснительной."
    y "У меня не было ни малейшего понятия, что вообще от него ожидать, но на тот момент я подумала, что это может быть именно то место, где я смогу немного сильнее раскрыться."
    y 2t "Никто не может быть осуждён за то, кто ты такой, это именно то, что ты мне сказала."
    y 2zi "И благодаря тебе, с каждым днём, как я приходила в клуб после школы, я чувствовала себя всё менее и менее незащищённой."
    y 1t "Так что, пожалуйста... не ссорьтесь вот так. Да вообще не ссорьтесь."
    y "Как [player] уже говорил, мы все здесь друзья, и мы все должны поддерживать друг друга."
    y 1zi "Я не против, если наш клуб так и останется маленьким, в какой-то степени, может, это даже и к лучшему."
    y "Кому нужны десятки и сотни участников клуба, если нам и сейчас и впятером всем комфортно?"
    show yuri 1s at t33 zorder 4
    "Вся комната погружается в тишину. Скорее всего, после столь вдохновленного монолога у каждого теперь очень смешанные чувства."
    show yuri at thide zorder 4
    hide yuri
    "Юри садится обратно, и для меня заметно, что она немного нервничает."
    show monika at f21 zorder 4
    show natsuki at t22 zorder 3
    m "..."
    show monika at t21 zorder 3
    show natsuki 5u at f22 zorder 4
    n "..."
    n 5n "Моника..."
    play music t9
    n 1m "П{w=0.25}.{w=0.25}.{w=0.25}. Прости."
    n "Было неправильно кричать на тебя."
    show natsuki 1n at t22 zorder 3
    show monika 1g at f21 zorder 4
    m "Нет, всё нормально."
    m "Я должна была сказать об этом всем вам, это только моя вина."
    m 2g "Но [player] и Юри правы, мы не должны наседать на глотки друг другу."
    m 1y "Мы должны дорожить тем, что у нас уже есть, и как далеко мы уже зашли как клуб."
    show monika 1e at t21 zorder 4
    "[persistent.sayoriname] выходит напротив всех нас, и мы все ждём, что же она скажет."
    show monika at t32 zorder 2
    show natsuki at t33 zorder 3
    show sayori 2zc at f31 zorder 4
    s "Я чувствую себя намного счастливее с тех пор, как мы подружились."
    s 1h "Правда в том, что... до того, как я вступила в клуб, я была совсем одна."
    s "[player] и я не разговаривали настолько часто, как мы это делаем сейчас."
    s 2h "У меня почти что и не было дел. Каждый день одно и то же..."
    s 1zc "Но тогда я встретила Монику в этом кабинете, и я решила дать этому клубу шанс."
    s "Она помогла мне избавиться от одиночества, а затем я встретила и всех остальных."
    s 4zc "Вы и правда очень много для меня значите, ребята."
    show sayori 4d at t31 zorder 4
    "Я н ожидал, что она закатит такую речь."
    "Она замечательна. Правда, очень."
    mc "Спасибо тебе, [persistent.sayoriname]."
    mc "Ты очень хорошо всё сказала, мне даже и добавить нечего."
    show sayori 1d at t31 zorder 3
    mc "Мы должны оставить это всё позади и простить друг друга."
    mc "Думаю, никто из нас не хочет, чтобы это продолжалось ещё дольше, чем мы уже имеем на данный момент."
    show natsuki 5s at f33 zorder 4
    n "..."
    n 5q "Я прощаю тебя, Моника."
    show natsuki 5s at t33 zorder 2
    show monika 1y at f32 zorder 4
    m "Я тоже тебя прощаю."
    m "И спасибо вам, [player], Юри и [persistent.sayoriname]."
    show monika 1e at t32 zorder 3
    show sayori 4r at t31 zorder 3
    "Ну что же, это было довольно неожиданно."
    "Но, если быть до конца честным, у меня и так были некие предположения насчёт всего этого."
    scene bg black with dissolve_scene_full
    "После того, как обстановка слегка разрядилась, мы все вернулись на свои места."
    scene bg club_day with dissolve_scene_full
    pause(1.0)
    show sayori 2h at f11 zorder 4
    s "[player], как ты себя чувствуешь, лучше?"
    show sayori 2g at t11 zorder 4
    mc "Да, спасибо тебе."
    show sayori 1d at t11 zorder 4
    mc "Возможно, стоило сказать раньше о том, что у меня есть некоторые проблемы с контролем гнева."
    mc "Но я просто не могу ничего не делать и не говорить, когда они так яростно спорят."
    mc "Но есть что-то, что я бы хотел, чтобы ты знала."
    mc "Ты тогда чувствовала какую-то дрожь, или всё же нет?"
    show sayori 1c at f11 zorder 4
    s "Да."
    s "Что это такое было?"
    show sayori 1b at t11 zorder 4
    mc "Может быть, именно так этот мир реагирует на мои эмоции."
    mc "Или я просто подсознательно сделал что-то, что стало этому причиной."
    show sayori 2c at f11 zorder 4
    s "Я думала, что я была единственной, кто заметил это."
    s 4h "Было даже немного страшно..."
    show sayori 4g at t11 zorder 4
    mc "Ну... Я не могу гарантировать того, что этого никогда снова не произойдёт."
    mc "Но кажется, это совсем не опасно."
    mc "Ладно, будем ли мы говорить с Юри по поводу того, что мы запланировали?"
    show sayori 1x at f11 zorder 4
    s "Я только хотела об этом у тебя спросить."
    show sayori 1a at t11 zorder 4
    mc "Приму это как «да»."
    scene bg club_day with wipeleft_scene
    stop music fadeout 2.5
    "Мы подходим к Юри, которая, по всей видимости, уже погрязла в своей книге."
    show sayori 1b at t21 zorder 4
    show yuri 2g at t22 zorder 3
    "Она нас не замечает."
    show sayori 2c at f21 zorder 4
    s "Юри?"
    show sayori 2b at t21 zorder 3
    show yuri 1n at f22 zorder 4
    y "Ах!"
    y 1q "Я не видела вас, простите."
    play music t8
    y 2f "Что вам будет угодно от меня?"
    show yuri 2e at t22 zorder 4
    show sayori 1a at t21 zorder 3
    mc "Мы просто хотели спросить, свободна ли ты сегодня после клуба."
    show yuri 1f at f22 zorder 4
    y "Да, свободна."
    y "Но почему вы спрашиваете?"
    show yuri 1e at t22 zorder 3
    show sayori 2x at f21 zorder 4
    s "Мы подумали, что мы могли бы сходить куда-нибудь вместе."
    show sayori 2a at t21 zorder 3
    show yuri 2o at f22 zorder 4
    y "Сходить куда-нибудь вместе? Но почему вы хотите пойти со мной?"
    show yuri at t22 zorder 3
    show sayori 1h at f21 zorder 4
    s "Ну... Тебе, кажется, одиноко."
    s 2c "Н-не в плохом смысле! Мы всего лишь хотим провести время с тобой."
    show yuri 2t at t22 zorder 3
    s 1zc "Ну же, будет весело!"
    show sayori 1d at t21 zorder 3
    mc "И к тому же... как ты уже и сама сказала, у тебя в твоём расписании больше ничего нет, ведь так?"
    show yuri 1q at f22 zorder 4
    y "Н-ну да..."
    show yuri at t22 zorder 3
    show sayori 2x at f21 zorder 4
    s "Мы можем пойти куда твоей душе будет угодно!"
    s 1c "Ну, кроме каких-то формальных мест."
    show sayori 1b at t21 zorder 3
    show yuri 2e at f22 zorder 4
    y "А?"
    show yuri at t22 zorder 4
    mc "Это из-за меня, мне там просто неудобно находиться."
    mc "Я уже говорил с [persistent.sayoriname] на эту тему раньше, так что она уже знает."
    show yuri 2b at f22 zorder 4
    y "Ох, ну ладно тогда."
    y "У меня есть на примете одно местечко, которое не особо формальное."
    y 1b "Ресторанчик недалеко отсюда."
    show yuri 1a at t22 zorder 3
    show sayori 2c at f21 zorder 4
    s "Кажется, я знаю, о каком именно ресторанчике ты говоришь."
    show sayori 2b at t21 zorder 4
    mc "Ну, а я нет."
    mc "Но это и не удивительно."
    show sayori 1a at t21 zorder 3
    show yuri 2f at f22 zorder 4
    y "Ты точно уверен, что не помнишь?"
    show yuri 2e at t22 zorder 4
    mc "Я даже более, чем точно уверен, что не помню."
    show sayori 1q at t21 zorder 3
    show yuri 2e at t22 zorder 4
    "Юри смотрит на меня с озадаченным выражением лица, в то время как [persistent.sayoriname] прекрасно знает, почему."
    show yuri 1q at f22 zorder 4
    y "Ах, ну конечно!"
    y "Как я вообще могла забыть такое?"
    show yuri 1u at t22 zorder 3
    show sayori 2x at f21 zorder 4
    s "Не переживай, ты не одна такая!"
    show sayori 2a at t21 zorder 3
    "Это делает объяснение намного легче, чем могло бы быть, если бы у них обеих не было представления о том, кто я такой на самом деле."
    mc "Да, то же самое приключилось и с [persistent.sayoriname] незадолго до этого."
    mc "Но если мы повторим наш визит, я прекрасно запомню это место, можешь на это рассчитывать."
    show yuri 2f at f22 zorder 4
    y "У тебя фотографическая память?"
    show yuri 2e at t22 zorder 4
    show sayori 1b at t21 zorder 4
    mc "Нет, но когда я усиливаю своё внимание, я смогу запомнить любое место или событие с предельной ясностью."
    mc "Можно сказать, что это даже лучше, чем фотографическая память."
    show sayori 4x at f21 zorder 4
    s "Это просто прекрасно, [player]!"
    show sayori 4a at t21 zorder 4
    mc "Это, безусловно, полезно, и самое лучшее в этом – это то, что я смогу так делать, только когда сфокусируюсь."
    mc "Это предотвращает меня от тех воспоминаний, о которых я попросту не хочу помнить."
    show sayori 1a at t21 zorder 3
    show yuri 1j at f22 zorder 4
    y "Если бы у меня такое только было..."
    show yuri 1i at t22 zorder 3
    show sayori 2x at f21 zorder 4
    s "Да! С этим умением школа бы была сущим пустяком."
    s "Я могла бы просто прочитать что-нибудь, а потом вспомнить это на экзамене."
    s 4r "100/100 баллов было бы просто лёгкой прогулкой для меня!"
    show sayori 4q at t21 zorder 4
    mc "Ну, с этим умением ты могла бы достичь гораздо большего, чем просто выпуститься из школы с аттестатом с отличием."
    show sayori 1a at t21 zorder 4
    mc "Было важно для меня развить иммунитет ко всякого рода манипуляциям и контролю."
    mc "Если бы кто-нибудь заполучил мою силу, кто знает, что бы они с ней сделали..."
    show sayori 1g at t21 zorder 3
    show yuri 2f at f22 zorder 4
    y "Есть и другие, которые тоже применяют способности?"
    show yuri 2e at t22 zorder 3
    mc "Мои способности уникальны, но многие люди из нашего мира тоже способны использовать свою силу."
    mc "К счастью, я самый сильный человек в нашем мире."
    mc "Даже если бы все люди в мире ополчились против меня, я бы всё равно переиграл их и уничтожил, даже не вспотев."
    show sayori 2h at f21 zorder 4
    s "Это даже немного страшно..."
    show sayori 2g at t21 zorder 4
    mc "Ну да, и это отчасти объясняет, почему многие люди в моём мире боятся меня."
    mc "Но я безумно рад тому, что вы, ребята, не боитесь."
    show sayori 1d at t21 zorder 4
    show yuri 1a at t22 zorder 3
    mc "Даже некоторые мои друзья говорят, что они попросту не могут не бояться меня, когда я рядом."
    mc "Даже несмотря на то, что я не плохой человек, я бы никогда не использовал эти способности, чтобы навредить тому, кто этого не заслуживает."
    mc "Можете говорить всё, что угодно, но, увы, пока ты сильный, некоторые люди всё равно будут бояться тебя."
    show sayori 2zc at f21 zorder 4
    s "О-о-о, тебе незачем переживать, [player]."
    s "Мы не боимся, и ты замечательный человек!"
    show sayori 2d at t21 zorder 3
    "Я невольно пророняю слезу после того, как она это говорит."
    show yuri 2b at f22 zorder 4
    y "Ты был очень мил и добр к нам, почему мы должны бояться тебя?"
    y 1h "И если бы ты хотел навредить нам, то ты бы уже давно это сделал."
    show yuri 1g at t22 zorder 4
    mc "Ну да... Всё верно..."
    mc "Спасибо вам обоим огромное, для меня это значит гораздо больше, чем вы сможете себе представить."
    mc "Будучи окружённым людьми, которые не видят в тебе источник угрозы – это очень здорово."
    scene bg black with dissolve_scene_full
    "Проходит время, и мы идём домой, чтобы подготовиться."
    "По пути в ресторанчик, я оглядываюсь вокруг, чтобы запомнить как можно больше, когда мне это понадобится."
    scene bg cafe with dissolve_scene_full
    "Я сажусь рядом с [persistent.sayoriname], а Юри – напротив нас."
    show sayori 4bx at f21 zorder 4
    show yuri 1ba at t22 zorder 3
    s "Ух ты! Это место выглядит намного лучше, чем я помню с прошлого раза."
    show sayori 4ba at t21 zorder 4
    mc "Мне тоже очень нравится, да и людей не так много."
    mc "По-моему, нам быстро принесут заказ."
    show sayori 1ba at t21 zorder 3
    show yuri 2bb at f22 zorder 4
    y "Да, а ещё они очень хорошо готовят."
    y "Это мой любимый ресторан в округе."
    show yuri 2ba at t22 zorder 3
    show sayori 1bx at f21 zorder 4
    s "У меня нет сомнений, что их еда невероятно вкусная!"
    show sayori 1ba at t21 zorder 4
    "Я мысленно хихикаю."
    mc "В этом мире вообще есть еда, которую ты не найдёшь вкусной?"
    show yuri 1bc at t22 zorder 3
    show sayori 5bd at f21 zorder 4
    s "Злюка!"
    show sayori at t21 zorder 3
    show yuri 1bd at f22 zorder 4
    y "Хе-хе, [persistent.sayoriname] найдёт вкусным что-угодно, если это можно употребить в пищу."
    show yuri 1bc at t22 zorder 3
    show sayori 1bl at f21 zorder 4
    s "Ничего не могу с собой поделать, мне нравится много кушать."
    s 1bx "Ребят, что будем заказывать?"
    show yuri 1ba at t22 zorder 3
    s 2bx "Не переживайте, весь счёт будет на мне."
    show sayori 2ba at t21 zorder 4
    mc "А ты уверена, что взяла с собой достаточно?"
    show sayori 1bx at f21 zorder 4
    s "Уж поверь мне, да."
    show sayori 1ba at t21 zorder 4
    mc "Я могу разделить с тобой счёт напополам. Так, на всякий случай."
    mc "Тогда это будет честно, да и к тому же, по какой-то странной причине люди из вашего мира расплачиваются теми же деньгами, что и люди из моего."
    mc "И плюс ко всему, у меня тоже с собой достаточно."
    show sayori 2bc at f21 zorder 3
    s "Вот так совпадение."
    s "Ладно, так что будем заказывать?"
    show sayori 2bb at t21 zorder 3
    show yuri 2bb at f22 zorder 4
    y "Думаю, я закажу Мисо Суп."
    show yuri 2ba at t22 zorder 3
    show sayori 1bx at f21 zorder 4
    s "А ты, [player]?"
    show sayori 1ba at t21 zorder 4
    mc "Ну... У меня возникают трудности с тем, чтобы опознать большинство из блюд."
    mc "Но я вижу, что у них есть Спагетти, одно из моих любимых блюд, поэтому я возьму это."
    show sayori 4br at f21 zorder 4
    s "Хорошо!"
    s 2bx "А я тогда возьму..."
    show sayori 1bo at t21 zorder 4
    "Она долго смотрит на меню, прежде чем выбирать."
    "Это ровно то, что я от неё и ожидал."
    show sayori 1bp at f21 zorder 4
    s "Так много вариантов!"
    s 2bn "О, у них есть картошка фри с рыбой!"
    s 1bx "Думаю, её я и возьму."
    show sayori 1ba at t21 zorder 4
    mc "Отличный выбор."
    scene bg black with dissolve_scene_full
    "К нам подходит официант, и мы делаем заказ."
    scene bg cafe with dissolve_scene_full
    show sayori 1ba at t21 zorder 3
    show yuri 1bb at f22 zorder 4
    y "[player], у меня к тебе вопрос."
    y "Как вообще выглядит твой мир?"
    show yuri 1ba at t22 zorder 4
    mc "Хм... Довольно неожиданно."
    mc "С чего бы вообще начать..."
    mc "Вообще, он во многом похож на ваш мир."
    mc "Главным различием является то, что у многих из нашего мира обладают какими-то способностями."
    show sayori 1bb at t21 zorder 3
    show yuri 1be at t22 zorder 4
    mc "Кто-то может сказать, что это опасно, для многих иметь способности, но на самом деле, всё даже наоборот."
    mc "Едва ли кто-то использует свои способности со злым умыслом."
    mc "А даже если и бывали такие случаи, я бы с лёгкостью смог одолеть таких людей."
    mc "Быть может, я частично и есть причина тому, почему это так необычно..."
    show yuri 1be at t22 zorder 3
    show sayori 1bc at f21 zorder 4
    s "Ты говоришь, что многие смогут научиться этим способностям..."
    s "А мы сможем обучиться этому?"
    show sayori 1bb at t21 zorder 4
    mc "Ну..."
    mc "С достаточной волей всё возможно, даже самое невозможное."
    mc "Когда ты прикладываешь достаточно усилий, тогда у вас будет шанс изменить свои судьбы."
    mc "Воля – это вообще-то источник силы, и, скорее всего, это причина, почему я самый сильный, потому что у меня самая сильная воля."
    mc "И я верю, что воля к сопротивлению – это самое мощное."
    mc "Кто знает, может, кто-то из вас обладает такой волей, а может, обе из вас обладают такой волей, и нужно только это выяснить."
    show yuri 1bf at f22 zorder 4
    y "Как бы ты описал волю к сопротивлению?"
    show yuri 1be at t22 zorder 4
    mc "Кажется, я знаю, как её описать..."
    mc "У вас когда-нибудь были ссоры с родителями, где они заставляли соблюдение какого-то правила?"
    show yuri 2bh at f22 zorder 4
    y "Насколько я помню, только когда я была маленькой."
    show yuri 2bg at t22 zorder 3
    show sayori 4br at f21 zorder 4
    s "Мои родители всегда заставляли меня, я была очень непослушным ребёнком!"
    show yuri 2be at t22 zorder 3
    s 1bc "Но иногда это как будто было даже нечестно."
    show sayori 1bb at t21 zorder 4
    mc "В таком случае, у тебя могло бы возникнуть желание сопротивляться им."
    mc "Кто-то, у кого есть воля к сопротивлению, этого не боится, и не важно, кому они противостоят."
    mc "Они преследуют их цель, и если кто-то или что-то встаёт у них на пути, они борются против этого, пока они не заполучат успех."
    mc "Если я хочу что-то сделать, я это сделаю эффективно. Вот как я бы описал эту волю."
    show sayori 2bc at f21 zorder 4
    s "А разве это не сделало бы тебя, ну... немного непокорным?"
    show sayori 2bb at t21 zorder 4
    mc "Да, и не немного, [persistent.sayoriname]."
    mc "Я попросту отказываюсь от всего, что я не хочу, до тех пор, пока я сам того не пожелаю."
    mc "Тебе не нужно сильно переживать из-за того, что я буду очень забывчивым и рассеянным к тому, что другие говорят мне."
    mc "В любом случае, я хочу сказать, что вы точно так же сможете использовать свои силы, как и я."
    mc "Если ты {b}на самом деле{/b} чего-то хочешь, тогда, я думаю, что вы и сможете."
    show sayori 4br at f21 zorder 4
    s "Это было бы так здорово!"
    show yuri 1ba at t22 zorder 3
    s 4bx "Я смогла бы тебя защитить!"
    show sayori 4ba at t21 zorder 4
    mc "Ха-ха, меня не нужно защищать, [persistent.sayoriname]."
    mc "Но я ценю то, насколько ты великодушна."
    show sayori 1ba at t21 zorder 3
    show yuri 1bj at f22 zorder 4
    y "На самом деле, было бы невероятно полезно иметь что-то вроде этого."
    y 1bf "Я вот думаю, какие же способности вообще есть."
    show yuri 1be at t22 zorder 4
    mc "Обычно они разделяются на атакующие, защитные и поддерживающие."
    mc "Но с достаточно сильной волей, тебе подвластно что-угодно."
    mc "Что-то вроде путешествия в другой мир высасывает очень много энергии из тебя."
    mc "Большинство даже и одного путешествия не смогут, даже со всей энергией, да и я смогу выполнить только 3 прыжка, а затем мне нужно отдохнуть."
    mc "Но кроме того... Это действительно завораживающе, что вы обе настолько открыты к этому диалогу."
    mc "Должно быть, это до сих пор чувствуется... странно."
    show sayori 1bc at f21 zorder 4
    s "Да, я никогда ни о чём подобном даже не слышала, пока ты сам мне об этом не сказал."
    s "Но я знаю, что это правда, я сама это увидела."
    s 2bx "А если человек с такими способностями – это ты, то мне не о чем бояться."
    show sayori 2ba at t21 zorder 3
    show yuri 2bzi at f22 zorder 4
    y "Согласна, ты заставил чувствовать себя лучше после того, как я с тобой поделилась своей проблемой."
    show yuri 2bs at t22 zorder 3
    show sayori 1bc at f21 zorder 4
    s "Юри, у тебя тоже какие-то проблемы?"
    show sayori 1bb at t21 zorder 3
    show yuri 2bv at f22 zorder 4
    y "..."
    y 2bt "Да."
    y 2bv "И не думаю, что готова поделиться этим с кем-угодно – только [player]."
    show yuri at t22 zorder 3
    show sayori 2bzc at f21 zorder 4
    s "Всё в порядке."
    s "Но пожалуйста, дай мне знать, когда ты будешь готова поделиться этим, Юри."
    show sayori 1bd at t21 zorder 3
    show yuri 1bzi at f22 zorder 4
    y "Спасибо."
    show yuri 1bs at t22 zorder 4
    mc "Вы обе очень понимающие, и это то, что я в вас ценю."
    mc "Это здорово, когда никто не подталкивает тебя, когда перед тобой сложная ситуация."
    show sayori 4bx at f21 zorder 4
    s "Я хочу, чтобы все были счастливы, и если Юри будет чувствовать себя лучше, если она повременит с этим, то тогда я в порядке."
    s 1bh "Потому что я прекрасно знаю, что это такое, скрывать сложную проблему."
    show sayori 1bg at t21 zorder 3
    show yuri 2bt at f22 zorder 4
    y "А ты поделилась ею со мной."
    y "Теперь мне даже немного стыдно, что я не делаю точно так же."
    show yuri 2bzg at t22 zorder 3
    show sayori 1bzc at f21 zorder 4
    s "Юри, я и правда не против."
    s "Тебе не нужно чувствовать себя плохо или неудобно, если тебе нужно ещё немного времени, и я уверена, что и [player] согласится."
    show sayori 1bd at t21 zorder 4
    mc "Она права, даже если бы я..."
    mc "Ну, я должен был... ну, знаешь..."
    show sayori 1bb at t21 zorder 3
    show yuri 2bzi at f22 zorder 4
    y "Нет, ты всё правильно сделал."
    y 2bt "Кто знает, что бы могло случиться, если бы ты этого не сделал."
    show yuri at t22 zorder 3
    show sayori 1bc at f21 zorder 4
    s "Ребят, о чём вы вообще говорите?"
    show sayori 1bb at t21 zorder 3
    show yuri 1bzi at f22 zorder 4
    y "[player] сказал, чтобы я не утаивала мой секрет от него, но это только потому что он и так уже знал о нём."
    show yuri 1bs at t22 zorder 3
    show sayori 2bc at f21 zorder 4
    s "Он знал и о моём секрете тоже."
    show yuri 1be at t22 zorder 3
    s 2bh "[player], что ты {i}на самом деле{/i} знаешь о нас?"
    show sayori 2bg at t21 zorder 4
    mc "Я не всезнающий, так что можете на этот счёт не переживать."
    mc "Но я знаю больше, чем смогу вам рассказать."
    mc "Если бы я сказал вам всё, это могло бы очень плохо на вас повлиять."
    mc "А я очень не хочу рисковать этим, я слишком вас ценю."
    show sayori 1bzc at f21 zorder 4
    s "Хорошо, я понимаю."
    show sayori 1bd at t21 zorder 3
    show yuri 2bf at f22 zorder 4
    y "Да, ты, скорее всего, прав."
    y 1bh "Иногда, если мы чего-то не знаем, это даже и лучше."
    y "Меньше знаешь – крепче спишь, как говорится."
    y 2bt "Я больше беспокоюсь о тебе, знать что-то подобное может отрицательно повлиять на твоё психическое здоровье."
    show yuri 2bzg at t22 zorder 3
    show sayori 1bg at t21 zorder 4
    mc "Тебе не о чем беспокоиться, я абсолютно здоров в психическом плане."
    mc "В те моменты, когда большинство просто ломаются, я держусь."
    mc "Это очень полезно в контексте текущей ситуации."
    show yuri 2bs at t22 zorder 3
    show sayori 1bd at t21 zorder 4
    mc "Но несмотря на это, это всё ещё заставляет чувствовать себя намного лучше, что вы обе хотите сражаться со своими скелетами в шкафу."
    show sayori 2bzc at f21 zorder 4
    s "Я обещала, что буду стараться."
    show sayori 2bd at t21 zorder 3
    mc "Ты же знаешь, что это в первую очередь нужно тебе, a не мне."
    mc "Но если это помогает тебе, то я не против."
    show yuri 1bt at f22 zorder 4
    y "Я могу понять, почему, потому что я чувствую примерно то же самое."
    y "Нет ничего и никого, чтобы помочь как-то с моей проблемой, только ты."
    y 2bzi "Ты сказал мне, что никогда не поздно, и я не могу это забыть."
    show sayori 1ba at t21 zorder 4
    show yuri 2bs at t22 zorder 3
    mc "Ну... Пока вы чувствуете себя хорошо, тогда это всё, что значит."
    mc "Даже если вы делаете больше для меня, чем для вас самих."
    mc "И я не хочу подталкивать вас к изменениям, если вы и сами не готовы к тому, чтобы поменяться."
    scene bg black with dissolve_scene_full
    "Пока я заканчиваю говорить, официант приносит наш заказ."
    "Мы все мирно едим и наслаждаемся уникальным вкусом блюд."
    scene bg cafe with dissolve_scene_full
    show sayori 1bq at t21 zorder 4
    show yuri 1ba at t22 zorder 3
    mc "Это было поистине великолепно, теперь я могу понять, почему это твой любимый ресторан, Юри."
    show sayori 4bx at f21 zorder 4
    s "Да! Я не наедалась так уже очень давно!"
    show sayori 4ba at t21 zorder 3
    show yuri 2bd at f22 zorder 4
    y "Я всегда наслаждаюсь трапезой здесь."
    y 1bb "И учитывая, насколько замечательно это на вкус, это место достаточно недорогое."
    show yuri 1ba at t22 zorder 3
    mc "Это лучше, чем большинство блюд из моего мира, и к тому же дешевле большинства из них."
    mc "Спасибо тебе за то, что рассказала нам об этом месте, без сомнений, я приду сюда ещё раз."
    show sayori 2bx at f21 zorder 4
    s "Мы можем сходить сюда ещё раз, если хочешь."
    s 4br "Я была бы не против отобедать здесь ещё раз!"
    show sayori 4bq at t21 zorder 4
    mc "Тогда решено. Что насчёт пятницы? Пятничные вечера – это всегда весело и увлекательно."
    show sayori 1ba at t21 zorder 3
    show yuri 2bq at f22 zorder 4
    y "М-могу ли я пойти с вами?"
    show yuri 2bu at t22 zorder 4
    mc "Ну конечно, и к тому же, я уверен, что ты захочешь позадавать мне ещё больше вопросов, ха-ха."
    scene bg black with dissolve_scene_full
    "Как я и предполагал, у [persistent.sayoriname] с собой было не так уж и много."
    "Мы разделили счёт пополам и вышли на улицу."
    stop music fadeout 2.5
    scene bg street_late with dissolve_scene_full
    pause(1.0)
    show sayori 1ba at t21 zorder 3
    show yuri 2bzi at f22 zorder 4
    play music t9
    y "Спасибо вам двоим, что вывели меня сегодня на прогулку."
    y "Вы сделали мой день, даже несмотря на то, что я поначалу отказалась."
    show yuri 2bs at t22 zorder 3
    show sayori 2bzc at f21 zorder 4
    s "В любое время, Юри!"
    s 1bc "Кажется, нам нужно уже расходиться, но я не знаю, где ты живёшь."
    show sayori 1bb at t21 zorder 3
    show yuri 2bf at f22 zorder 4
    y "Я живу на другом конце города, так что сейчас мы точно расходимся."
    y 1bb "Но мы всегда увидимся завтра."
    show yuri 1ba at t22 zorder 3
    show sayori 1ba at t21 zorder 4
    mc "Да, и надеюсь, без всяких споров."
    show yuri 1bu at t22 zorder 3
    show sayori 2bl at f21 zorder 4
    s "Хе-хе... да-а-а..."
    s 1bh "Я уверена, что никто этого не хочет, и это плохо влияет на всех нас."
    s "Не могу себе представить, как зол ты был внутри, [player]."
    show sayori 1bg at t21 zorder 4
    show yuri 1bzg at t22 zorder 3
    mc "Это только внешне кажется, что я был зол, но на самом деле я ощущал разочарование и грусть."
    mc "Мы все только поладили в субботу, а потом происходит...{w=0.6} {b}вот это{/b}."
    mc "А всё из-за фестиваля."
    show yuri 2bt at f22 zorder 4
    y "Честно, я хотела встать и сделать то же самое, что сделал ты."
    y 2bv "Но я просто не могла, у меня не хватило силы, чтобы это сделать."
    show yuri at t22 zorder 4
    mc "Мы все работаем по-разному, так что не нужно себя винить за это."
    mc "Это просто не твоя личность, чтобы вот так взрываться гневом и дать своим эмоциям вырваться наружу."
    show sayori 2bzc at f21 zorder 4
    s "Ты слишком нежная и добрая, Юри."
    s "Я знаю, что ты хочешь, чтобы между нами было всё хорошо."
    s 1bzc "И я это поняла, когда ты встала после того, как [player] закончил говорить."
    show sayori 1bd at t21 zorder 3
    show yuri 1bt at f22 zorder 4
    y "Но я всё ещё нервничала, и внутри я совсем не была уверена в этом."
    y "Я бы определённо остановилась, если бы [player] не подбодрил меня, чтобы я продолжила."
    show yuri 1bzg at t22 zorder 4
    mc "Что на самом деле важно, как это смысл, который ты вкладываешь в свои слова, и что они отражают."
    mc "Что ты хочешь доказать, и над чем ты хочешь, чтобы все задумались."
    mc "В конце концов, мы всё-таки убедили их не ссориться."
    show yuri 1bq at f22 zorder 4
    y "По большей части это благодаря тебе."
    y "Ты был первым, кто вмешался, я даже могла почувствовать, что ты сделал это без задней мысли."
    show yuri 1bu at t22 zorder 4
    mc "У тебя хорошая интуиция. Это просто то, как моя личность вообще работает."
    mc "Обычно я не особо разговариваю с людьми, но если есть что-то, о чём просто невозможно молчать, я просто делаю это и ни о чём не жалею."
    show yuri 1bt at f22 zorder 4
    y "Если бы я только смогла быть как ты, ты же такой сильный."
    y "И физически, и психически."
    show yuri 1bzg at t22 zorder 3
    mc "Может быть и да, но это вовсе не означает, что ты не должна любить себя за то, кто ты есть."
    mc "Не пытайся быть мной, будь кем-то, кем ты сама могла бы гордиться."
    mc "Только так ты постигнешь лучшее состояние в своей жизни."
    show sayori 1bk at f21 zorder 4
    s "Я могу понять, почему для Юри это так сложно."
    s 1bh "Мне тоже трудно на самом деле любить себя."
    show sayori 1bg at t21 zorder 4
    mc "[persistent.sayoriname]..."
    show sayori 2bzc at f21 zorder 4
    s "Да не переживай ты, я ведь стараюсь."
    s 1bh "Но это всё равно сложно, даже зная о том, что ты любишь меня за то, какая я есть."
    show sayori 1bg at t21 zorder 4
    mc "..."
    mc "Если ты продолжишь давить, ты познаешь настоящее счастье от того, кто ты есть."
    mc "Вне зависимости от проблемы, пока ты этого хочешь, ты сможешь это сделать."
    mc "Я говорю это по личному опыту, я тоже проходил это."
    show sayori 1bd at f21 zorder 4
    s "..."
    s 2bzc "Я верю тебе, [player]."
    show yuri 1bs at t22 zorder 3
    s "И я продолжу, потому что ты веришь в меня, потому что ты любишь меня."
    s "И я не хочу тебя подвести."
    show sayori 1bd at t21 zorder 4
    mc "Вот это та [persistent.sayoriname], которую я знаю!"
    mc "То же самое касается и тебя, Юри."
    mc "Ты должна любить себя за то, кто ты есть, это самое важное для тебя, даже если сейчас ты не веришь."
    mc "Все сомнения могут говорить тебе, что они хотят, но когда ты наконец-то постигнешь, ты познаешь."
    mc "Ты будешь размышлять над этим, поймёшь это, и, наконец, будешь этим дорожить."
    show yuri 2bu at f22 zorder 4
    y "Я... я постараюсь."
    y 1bb "Но сейчас нам действительно нужно расходиться."
    y 1bd "Всегда есть любой другой день, когда мы можем поболтать."
    show yuri 1bc at t22 zorder 3
    show sayori 1bc at t21 zorder 4
    "[persistent.sayoriname], кажется, что-то внезапно вспомнила."
    show sayori 4bs at f21 zorder 4
    s "У меня есть замечательная идея на завтра!"
    s 2bzb "Но сейчас это сюрприз."
    show sayori 1ba at t21 zorder 4
    mc "Как же жаль, что я терпеливый человек, [persistent.sayoriname]."
    show sayori 5bd at t21 zorder 3
    show yuri 2bb at f22 zorder 4
    y "Я с нетерпением жду того, чтобы узнать, что же ты такого придумала."
    y 1bw "Надеюсь, что-то, что поможет нам всем забыть эту ссору."
    show sayori 1bg at t21 zorder 4
    show yuri at t22 zorder 3
    mc "События наподобие этого происходят вполне естественно, и лучший способ их решить – это просто забыть, что это когда-либо вообще происходило."
    mc "Никто ничего из этого не получит, тогда почему кто-то ещё хочет продолжать?"
    show sayori 2bzc at f21 zorder 4
    s "Да, всё будет в порядке, Юри."
    show sayori 2bd at t21 zorder 3
    show yuri 1bv at f22 zorder 4
    y "Ну, да, думаю, ты права."
    y 2bzi "В любом случае, увидимся с вами завтра."
    y 1bzi "Берегите себя."
    show yuri 1bs at t22 zorder 3
    show sayori 2br at f21 zorder 4
    s "До завтра!"
    show sayori 2bq at t21 zorder 4
    mc "Да, до завтра."
    scene bg living_room_late with dissolve_scene_full
    pause(1.0)
    show sayori 1ba at t11 zorder 4
    mc "Какой трудный день."
    mc "Но я рад, что вечером мы наконец-то сможем расслабиться."
    show sayori 2bc at f11 zorder 4
    s "Да, меня очень удивило то, что происходило сегодня."
    s 1bc "Я вообще не ожидала, что ты отреагируешь вот так."
    s 1bk "У меня даже мелькали мысли, что ты мог бы..."
    show sayori at t11 zorder 4
    mc "[persistent.sayoriname], ты же знаешь, что я сделаю всё, что в моих силах, чтобы этого не произошло, так ведь?"
    mc "Никто не должен пострадать от того, что чувствую я. Никогда."
    show sayori 2bh at f11 zorder 4
    s "Я не хочу, чтобы это произошло, и я верю, что ты постараешься."
    s 1bh "Но как ты и сам сказал, «ты никогда не знаешь»."
    s 4bv "А что, если ты в порыве гнева даже не сможешь отличить, кто я и где я?"
    show sayori 4bv at t11 zorder 4
    mc "Если это когда-нибудь и произойдёт..."
    mc "Пожалуйста, беги как можно быстрее и дальше, как только сможешь."
    mc "Потому что если я даже не смогу отличить, кто ты и где ты, тогда это означает, что мой разум затуманен ненавистью."
    mc "Я начну рвать и метать всё и вся, и никто меня не удержит."
    mc "Но я не дам этому случиться так легко, я слишком сильно о тебе забочусь."
    mc "Я даже не знаю, что бы я сделал, если бы я нанёс тебе или другим непоправимого ущерба."
    show sayori 1bt at f11 zorder 4
    s "..."
    s 1bzd "Я верю, что этого не случится."
    s 2bzc "А даже если я и увижу, что это случается, я изо всех сил постараюсь утешить тебя."
    show sayori 2bd at t11 zorder 4
    mc "Если бы ты это сделала, это было бы очень храбро и смело с твоей стороны."
    mc "[persistent.sayoriname], ты лучшая."
    show sayori 1bl at f11 zorder 4
    s "Н-нет, это не так..."
    show sayori 1by at t11 zorder 4
    mc "Да, это именно так."
    show sayori 1bd at t11 zorder 4
    mc "Чтобы сделать что-то подобное, это большее, чем просто мужество."
    mc "Но я постараюсь сделать так, чтобы этого в принципе никогда не произошло."
    mc "Я не хочу сделать тебе больно из-за меня."
    show sayori 2bzc at f11 zorder 4
    s "[player]..."
    s "Ты спас меня, ты сделал всё, что мог, чтобы я полюбила себя."
    s 1bzc "Это наименьшее, что я могу сделать."
    show sayori 1bd at t11 zorder 4
    mc "Для тебя это, может, и мало, но для меня – это очень многое."
    mc "Знать, что есть человек, который хочет тебе помочь, даже в самом худшем случае."
    mc "У меня прежде никогда не было такого чувства..."
    mc "Твоё умение заставить меня чувствовать, что меня ценят, никогда не перестанет удивлять меня."
    mc "Я безумно рад, что ты рядом, [persistent.sayoriname]."
    show sayori 4bs at t11 zorder 4
    "Я прижимаюсь к ней и обвиваю её руками."
    "Она заслуживает всю любовь в мире за то, что она делает для других."
    mc "Я хочу сделать {b}всё{/b}, чтобы ты чувствовала себя лучше."
    show sayori 4bd at t11 zorder 4
    mc "Такой человек, как ты, не заслуживает чего-то столь жестоко, как депрессия."
    show sayori 2bh at f11 zorder 4
    s "Никто не заслуживает, [player]."
    s "Это ощущение пустоты, бесполезности..."
    s "Я не хочу, чтобы хоть кто-то проходил через подобное, и поэтому я не хотела, чтобы ты обо мне заботился, ещё тогда, давно."
    s 1bh "Потому что я думала, что я бы каким-то образом и на тебя точно так же повлияла."
    show sayori 1bg at t11 zorder 4
    mc "[persistent.sayoriname]... Заботясь обо мне, ты не делаешь мне или кому-либо ещё хуже."
    mc "Наоборот, я почувствовал облегчение, что ты стала чувствовать себя лучше."
    mc "И мы пройдём через эту пустоту и тьму вместе."
    show sayori 1bd at t11 zorder 4
    mc "И я уверен, что Юри тоже старается заботиться о тебе."
    mc "Так что не думай, что нам всё равно, ты очень важна для нас."
    mc "Ты очень важна для меня..."
    show sayori 4bt at t11 zorder 4
    window hide
    pause(1.0)
    scene bg black with dissolve_scene_full
    "После долгого и тяжёлого дня, мы с [persistent.sayoriname] ложимся спать."
    "Но прежде чем мы вошли в комнату, я получил новое сообщение."
    scene bg house_corridor_night with dissolve_scene_full
    show sayori 1pb at t11 zorder 4
    mc "А? Кто-то пишет мне."
    mc "Это{w=0.25}.{w=0.25}.{w=0.25}. Моника?"
    mc "Почему она пишет мне сейчас?"
    show sayori 1pc at f11 zorder 4
    s "Что она сказала?"
    show sayori 1pb at t11 zorder 4
    mc "Подожди, дай мне секундочку..."
    mc "..."
    mc "Она хочет, чтобы мы встретились у её дома."
    show sayori 2pc at f11 zorder 4
    s "Так поздно?"
    show sayori 2pb at t11 zorder 4
    mc "Я настолько же озадачен, как и ты."
    mc "Может, это что-то важное, тогда я пойду."
    mc "Я скоро вернусь, не переживай."
    show sayori 1pzc at f11 zorder 4
    s "Всё в порядке, убедись, что и она тоже в порядке."
    show sayori 1pd at t11 zorder 4
    mc "Конечно."
    scene bg black with dissolve_scene_full
    stop music fadeout 4.0
    "Я выхожу и быстро направляюсь в сторону дома Моники."
    scene bg house2_night with dissolve_scene_full
    "Моника уже там, смотрит на меня с очень грустным выражением лица."
    show monika 1bf at t11 zorder 4
    mc "Моника? Всё в порядке?"
    show monika 1bg at f11 zorder 4
    play music Eternity2
    m "[player]... Почему ты делаешь мне так больно?.."
    show monika 1bf at t11 zorder 4
    mc "Больно? Но я не делаю тебе больно, да и не хочу делать тебе больно."
    mc "О чём ты говоришь?"
    show monika 1bg at f11 zorder 4
    m "Вы с [persistent.sayoriname] так близки... и это так больно..."
    m 1bza "Почему она просто не может оставить тебя одного?!"
    show monika at t11 zorder 4
    mc "Довольно, Моника!"
    show monika 1bw at t11 zorder 4
    mc "Разве ты не видишь, что с тобой делает ревность?!"
    mc "Ты желаешь, чтобы нас не было друг у друга!"
    mc "Тебе не кажется, что это немножко неправильно?!"
    show monika at f11 zorder 4
    m "..."
    m 1bx "Я ничего не могу с собой поделать, [player]."
    m "Даже после того, как ты сказал, что у меня есть воля, чтобы пройти через это, я всё равно не могу ничего поделать..."
    m 1bz "Я не смогу сделать всего, чтобы быть с тобой."
    show monika at t11 zorder 4
    mc "Но ты и так со мной, каждый день, в клубе."
    mc "Мы даже разговариваем, даже прямо сейчас."
    show monika at f11 zorder 4
    m 1bx "Да, но ты не любишь меня."
    m "Ты не обнимаешь меня и не утешаешь меня."
    m 1bza "А всё из-за НЕЁ!"
    show monika at t11 zorder 4
    mc "Перестань говорить о [persistent.sayoriname], как будто это какая-то проблема!"
    show monika 1bw at t11 zorder 4
    mc "У неё тоже есть чувства, она такая же, как и ты."
    mc "Она так старается, чтобы все чувствовали себя лучше, ты можешь ценить хотя бы это?!"
    show monika 1bz at f11 zorder 4
    m "Но {b}{i}Я{/i}{/b} несчастная, [player]."
    show monika at t11 zorder 4
    mc "..."
    show monika 1bx at f11 zorder 4
    m "Всё, чего я хочу, это просто быть с тобой."
    m "Я бы пожертвовала всем, только чтобы ты меня полюбил."
    m "Ты проделал весь этот путь, чтобы всем помочь, несмотря на все риски."
    m "Этот мир даже не зависит от кого-то или чего-то, всё благодаря тебе."
    m 1bza "И тем не менее... ты выбрал {b}ЕЁ{/b}."
    m 1bzb "Зачем?! Почему?! Для чего?! Объяснишь мне?!"
    show monika 1bzc at t11 zorder 4
    mc "По всей видимости, ты не поймёшь."
    mc "По крайней мере, не в твоём текущем состоянии."
    mc "Я ценю и тебя тоже, и не то, чтобы я был здесь, чтобы мучить тебя."
    show monika 1bw at t11 zorder 4
    mc "Но ты не сможешь и просто не заставишь тебя полюбить меня, это просто неправильно."
    mc "Я знаю, что я не смогу всех сделать {i}одинаково{/i} счастливыми, потому что кто-то всегда будет против принятого мною решения."
    mc "Ты должна захотеть сражаться за это, я не смогу сделать это за тебя."
    show monika 1bx at f11 zorder 4
    m "{w=0.25}.{w=0.25}.{w=0.25}."
    m "Ничего не могу с собой поделать, оно до сих пор болит."
    m 1bz "Я недостаточно сильная..."
    show monika at t11 zorder 4
    mc "Ответ неверный. Ты гораздо сильнее, чем ты думаешь."
    mc "С достаточной волей ты добьёшься всего."
    mc "Ты не сможешь добиться ничего только тогда, когда твоя воля сломлена и разбита."
    mc "Но твоя воля всё ещё яркая, я уверен."
    show monika 1bw at f11 zorder 4
    m "..."
    m 1bx "Нет, никакая моя воля не яркая, [player]."
    m "Я пыталась навредить своим друзьям."
    m "Хотела, чтобы с ними произошли ужасные вещи."
    m "А сейчас я пытаюсь заставить тебя любить меня."
    m "Нет ничего в моей воле, вообще ничего."
    show monika 1bw at t11 zorder 4
    mc "Это потому что ты ещё не пыталась найти другой путь."
    mc "Твои мысли будут говорить тебе, что нет никакого другого пути..."
    mc "Но другой путь всегда есть, и ты обязательно его увидишь, когда присмотришься."
    mc "..."
    mc "Поздновато уже, пойду-ка я."
    mc "Подумай над тем, что я сказал."
    show monika 1bx at f11 zorder 4
    m "Пожалуйста... не уходи от меня..."
    show monika 1bw at t11 zorder 4
    mc "Прости, но я же не могу просто так стоять на холоде вечно."
    mc "Не будь настолько зависима от меня, так ты только больше себе навредишь."
    mc "А я не хочу тебе вредить, так что хотя бы попытайся."
    show monika at f11 zorder 4
    m "..."
    m 1bx "Да я только и делаю, что пытаюсь, но это никак не помогает."
    m "Я слишком слаба, чтобы превозмочь это самостоятельно..."
    m "А ты слишком сильный, мне не сравниться с твоей волей."
    show monika 1bw at t11 zorder 4
    mc "Ты всё не упускаешь возможности заставить меня быть с тобой, не так ли?"
    mc "Если это первая мысль, тогда ты так и не сможешь считать себя сильной и остановиться в текущем состоянии."
    mc "Это довольно веская причина, чтобы я наказал тебя."
    mc "Но я не буду, потому что я всё ещё верю, что ты изменишься."
    mc "Кто-угодно сможет, если он хотя бы попытается."
    mc "Увидимся завтра в школе, быть может, мы сможем приятно провести время после клуба."
    show monika 2bz at t11 zorder 4
    "Она медленно вытирает свои слёзы. Она выглядит полностью поверженной."
    show monika 2bp at f11 zorder 4
    m "Д-до з-завтра в ш-школе..."
    scene bg house_corridor_night with dissolve_scene_full
    stop music fadeout 3.0
    mc "Привет, [persistent.sayoriname], я вернулся."
    show sayori 2pc at f11 zorder 4
    s "Привет! Как всё прошло?"
    show sayori 2pb at t11 zorder 4
    mc "Плохо... очень плохо."
    show sayori 1pg at t11 zorder 4
    mc "Монике плохо как никогда раньше."
    mc "Я вообще не смог до неё достучаться, выглядит так, как будто она уже заранее сдалась в чём-то."
    mc "Я просто надеюсь, что что бы ты ни придумала, приободрило бы её, пусть даже и самую малость."
    show sayori 4px at f11 zorder 4
    s "Я думаю, ей понравится эта идея!"
    s 2px "Не переживай, я скажу тебе, но только после того, как мы доберёмся до клуба."
    show sayori 2pa at t11 zorder 4
    mc "Звучит здорово."
    mc "Но нам бы лучше поспать."
    mc "Честно говоря, я даже немного удивлён, что ты осталась дожидаться меня, несмотря на то, насколько рано ты засыпаешь."
    show sayori 1pr at f11 zorder 4
    s "Мне было бы удобнее, если бы ты спал рядом со мной."
    show sayori 1pq at t11 zorder 4
    mc "Хе-хе... Да, ты права."
    scene bg black with dissolve_scene_full
    "На следующее утро мы снова идём в школу."
    "Пока шли уроки, я думал о том, что же такого [persistent.sayoriname] придумала, чтобы помочь мне с тем, чтобы Моника чувствовала себя лучше."
    "Я знаю, что у Моники проблемы, даже если она сама не знает, насколько они серьёзны."
    "Но кто знает, может, она хотела помочь ей ещё чуть больше."
    "После всех уроков мы с [persistent.sayoriname] идём в клубную комнату."
    scene bg club_day with dissolve_scene_full
    show sayori 4x at f11 zorder 4
    play music t2
    s "Всем привет! Мы здесь!"
    show sayori 1a at t21 zorder 3
    show yuri 1b at f22 zorder 4
    y "Привет, [persistent.sayoriname]! Привет, [player]!"
    y "Как проходит ваш день?"
    show yuri 1a at t22 zorder 3
    mc "Помимо скучных уроков, я бы сказал, что вторники в целом ничего."
    show sayori 4p at f21 zorder 4
    s "У нас была физика и математика! Я ненавижу эти предметы!"
    show sayori at t21 zorder 4
    mc "Я тоже не люблю физику: она не только скучная, но ещё и невероятно сложная."
    mc "А математика сойдёт, пока примеры не очень замудренные."
    show sayori 2j at f21 zorder 4
    s "Поэтому я и ненавижу физику! Она слишком сложная, и от неё у меня голова болит!"
    show sayori 2i at t21 zorder 3
    show yuri 2d at f22 zorder 4
    y "Это было ожидаемо от тебя, [persistent.sayoriname]."
    show yuri 2b at t22 zorder 3
    show sayori 5b at f21 zorder 4
    s "Хе-хе-хе..."
    show sayori at t21 zorder 3
    show yuri 1f at f22 zorder 4
    y "Я думала, что тебе это будет чуть более интересно, [player]."
    show yuri 1e at t22 zorder 3
    show sayori 1b at t21 zorder 4
    mc "Вовсе нет, я не люблю предметы, которые излишне сложные и научные."
    mc "И даже если я с лёгкостью смогу запомнить и решить их, это не совсем то, что бы вызвало мой интерес."
    mc "Я предпочитаю языки и что-то связанное с компьютерами."
    show yuri 1b at f22 zorder 4
    show sayori 1a at t21 zorder 3
    y "Полезно знать."
    y 2f "А вот лично я предпочитаю физику и химию."
    y 1b "Все эти реакции – это так восхитительно, чтобы изучать их и экспериментировать с ними."
    show yuri 1a at t32 zorder 2
    show sayori at t31 zorder 3
    show natsuki 2d at f33 zorder 4
    n "Привет, ребята! О чём шушукаетесь?"
    show natsuki 2j at t33 zorder 4
    mc "Да просто о предметах, которые нам нравятся и не нравятся."
    show natsuki 5w at f33 zorder 4
    n "Угх, мои учителя даже толком и не учат ничего."
    n 5q "Я ненавижу почти все предметы, которые у меня есть."
    show natsuki 5s at t33 zorder 2
    mc "Действительно хороший учитель – это большая редкость, большинство из них просто отрабатывают зарплату."
    mc "И даже если зарплата и не очень большая, они не настолько-то тяжело и работают."
    show yuri 1f at f32 zorder 4
    y "Да, думаю, ты прав."
    y "Людям предпочтительнее выбирать работу, на которой они ничего не будут делать, а получать много."
    y 1h "На самом деле, я даже не знаю, сколько учителя зарабатывают, но у них как минимум должно быть высшее педагогическое образование."
    y "Наверняка это куда больше минималки."
    show yuri 1e at t32 zorder 2
    show natsuki 1w at f33 zorder 4
    n "Да некоторые из них не заслуживают даже минималки!"
    n 1r "Всё, что они делают – это просто орут на тебя, если ты чего-то не понимаешь."
    show natsuki at t33 zorder 3
    show sayori 2c at f31 zorder 4
    s "Мои учителя не такие, они на самом деле довольно хорошие."
    s 1x "Мы даже смотрим интересные видосы время от времени!"
    show sayori 1a at t31 zorder 3
    show natsuki 5w at f33 zorder 4
    n "Везучая! Если бы у меня только были такие учителя."
    n 5q "Ну... У нас есть один такой, и он,{w=0.25} ну,{w=0.25} неплохой."
    n 1h "Но это только один из бог знает скольки, которые у нас есть."
    show natsuki 1g at t33 zorder 3
    show sayori 2x at f31 zorder 4
    s "Не переживай, Нацуки!"
    s "Я запланировала кое-что для нас всех!"
    s 1x "Я вам всем скажу, когда Моника придёт."
    show sayori 1a at t31 zorder 4
    mc "А где она вообще?"
    show sayori 1b at t31 zorder 3
    show yuri 2f at f32 zorder 4
    y "Я видела её перед тем, как войти в клубную комнату."
    y 1v "Но выглядело так, как будто она меня избегала, она даже не поздоровалась со мной."
    show yuri at t32 zorder 4
    "Ну конечно...{w=0.25} не поздоровалась...{w=0.25} конечно, блин..."
    mc "Ну, думаю, у неё просто трудный день."
    show yuri 1e at t32 zorder 4
    show natsuki 1za at t33 zorder 2
    "Внезапно Моника вваливается в клубную комнату, где мы все смотрим на неё."
    show monika 1p at f41 zorder 4
    show yuri at t43 zorder 2
    show sayori at t42 zorder 3
    show natsuki at t44 zorder 1
    m "Простите за то, что опять опоздала..."
    show monika 1o at t41 zorder 3
    show sayori 1c at f42 zorder 4
    s "Моника, чт-"
    show monika at thide zorder 3
    hide monika
    show sayori 1g at t31 zorder 4
    show yuri 1zg at t32 zorder 3
    show natsuki at t33 zorder 2
    "Моника быстро проходит и занимает место на учительском столе."
    mc "Бесспорно, у неё очень напряжённый день."
    show sayori 1k at f31 zorder 4
    s "Думаю, ты прав, она даже не ответила мне."
    s 1zc "Надеюсь, я слегка улучшу её настроение."
    show sayori 1d at t31 zorder 3
    "[persistent.sayoriname] – это, наверное, последний человек в клубе, которому стоит это делать, Моника, должно быть, будет ненавидеть её ещё больше..."
    "Нет сомнений, что Моника при первой же возможности навредила бы [persistent.sayoriname], если бы только могла."
    show yuri 2f at f32 zorder 4
    y "Так в чём заключается твоя идея, [persistent.sayoriname]?"
    show yuri 2e at t32 zorder 3
    show sayori 1n at f31 zorder 4
    s "..."
    s 2x "Забудьте! У меня есть идея получше!"
    s 1c "Но, [player], я хочу, чтобы это был сюрприз для тебя."
    s "Ты можешь поговорить с Моникой, пока я рассказываю всем остальным?"
    show sayori 1b at t31 zorder 4
    mc "Конечно. Наверное, это даже лучше."
    mc "Скажи нам, когда закончишь."
    show sayori 4r at f31 zorder 4
    s "Хорошо!"
    scene bg club_day with wipeleft_scene
    pause(1.0)
    show monika 1o at t11 zorder 4
    mc "Привет, Моника. Всё ещё думаешь об этом?"
    show monika 1g at f11 zorder 4
    m "А как я могу не думать об этом?"
    m "Я думала об этом целый день, и не могу остановиться."
    show monika 1f at t11 zorder 4
    mc "Принять это и двигаться дальше иногда бывает очень сложно, даже для полностью психически здорового человека."
    mc "Но [persistent.sayoriname] придумала кое-что, что может сделать твой день хоть чуточку лучше."
    show monika 2g at f11 zorder 4
    m "Я очень в этом сомневаюсь..."
    m "Она даже не догадывается, почему я так себя чувствую."
    show monika 2f at t11 zorder 4
    mc "Но это же не значит, что взбодрить тебя невозможно."
    mc "Просто попробуй, я же вижу, как она старается..."
    show monika 1c at t41 zorder 3
    show sayori 2x at f42 zorder 4
    show yuri 1a at t43 zorder 2
    show natsuki 5a at t44 zorder 1
    s "Итак, ребята! Я сказала им об этом."
    s "Но вы двое должны остаться после клубного собрания."
    s 1c "Моника, можешь ненадолго задержаться после того, как мы уйдём?"
    show sayori 1b at t42 zorder 3
    show monika 2o at f41 zorder 4
    m "..."
    m 2p "Думаю, я смогу, да..."
    show monika 2o at t41 zorder 3
    show sayori 4r at f42 zorder 4
    s "Ура!"
    s 4x "Тогда это все!"
    show sayori 1a at t42 zorder 3
    show monika 1d at f41 zorder 4
    m "Что мы будем делать?"
    show monika 1c at t41 zorder 3
    show sayori 4zb at f42 zorder 4
    s "Это сюрприз!"
    s 1x "Но я уверена, тебе понравится идея."
    show sayori 1a at t42 zorder 3
    show monika 2n at f41 zorder 4
    m "Ну, раз ты так говоришь..."
    scene bg black with dissolve_scene_full
    stop music fadeout 7.0
    "После того, как мы все покинули клубную комнату, мы все собираемся перед домом [persistent.sayoriname]."
    "Я замечаю, что Моника заметно нервничает по этому поводу."
    scene bg house with dissolve_scene_full
    show sayori 2x at f11 zorder 4
    s "А вот и все!"
    show sayori 2a at t21 zorder 3
    show natsuki 2d at f22 zorder 4
    n "А, так ты живёшь недалек от школы."
    n 1c "Было бы приятно иметь что-то подобное."
    show natsuki 1za at t22 zorder 3
    show sayori 2x at f21 zorder 4
    s "Ну да, тебе не нужно долго добираться до школы."
    s "Поэтому [player] и я успеваем плотно позавтракать перед тем, как пойдём в школу."
    s 1x "Ладно,, входите!"
    scene bg living_room with dissolve_scene_full
    show yuri 2f at f22 zorder 4
    show sayori 1a at t21 zorder 3
    y "Теперь, раз уж мы все здесь..."
    y 1v "М-можно я сначала скажу?"
    show yuri at t22 zorder 3
    show sayori 2r at f21 zorder 4
    s "Конечно!"
    show sayori at thide zorder 4
    hide sayori
    show yuri 2w at t11 zorder 4
    "Юри делает глубокий вдох и начинает свой монолог."
    show yuri 2u at f11 zorder 4
    play music t9
    y "Есть что-то, с чем я бы хотела поделиться со всеми вами."
    y 2t "Об этом н-нелегко говорить, и н-некоторые из вас будут шокированы, услыша это..."
    y 2v "Видите ли..."
    y 1t "[player] помогает мне превозмочь мою проблему."
    y 1w "..."
    y 2v "Правда в том, что{w=0.25}.{w=0.25}.{w=0.25}. Раньше я очень часто резала себя ножом..."
    show yuri at t21 zorder 3
    show natsuki 1p at f22 zorder 4
    n "ЧЕГО БЛЯТЬ?!"
    n "ЮРИ?! ПОЧЕМУ ТЫ РАНЬШЕ МНЕ ОБ ЭТОМ НЕ СКАЗАЛА?!"
    show natsuki at t22 zorder 3
    show yuri 2t at f21 zorder 4
    y "Я была ещё не готова... Прости..."
    show natsuki 1m at t22 zorder 3
    y 1zi "Но всё уже более-менее, я стараюсь прекратить."
    y "[player] и [persistent.sayoriname], благодаря им двоим, всё стало гораздо легче."
    y 2t "И мне правда очень жаль, что я не сказала тебе и Монике раньше, раньше у меня бы просто не хватило воли..."
    show yuri 2zg at t31 zorder 3
    show natsuki at t32 zorder 2
    show sayori 2zc at f33 zorder 4
    s "Я прекрасно тебя понимаю, Юри."
    s 1zc "Но не переживай, ты сможешь остановиться, а мы будем рядом, чтобы помочь!"
    show natsuki 1a at t32 zorder 2
    show sayori 1d at t33 zorder 3
    show yuri 1zi at f31 zorder 4
    y "Спасибо, [persistent.sayoriname]."
    y "Я хотела выразить благодарность: спасибо тебе, [player], ты сказал мне, что во мне есть силы сражаться."
    y 2zi "Ты призвал меня стараться изо всех сил. Если бы не ты, я бы просто не смогла остановиться."
    show yuri 2s at t31 zorder 2
    show natsuki 2t at f32 zorder 4
    n "Как же я тебя понимаю, Юри..."
    n 1m "Надо мной издевался мой папа, он меня часто бил, и вот поэтому я хотела хранить свою мангу в клубной комнате."
    show yuri 1t at t31 zorder 2
    show sayori 1g at t33 zorder 3
    n "Он бы тупо выбросил её, если бы я не..."
    n 5q "И я не сопротивлялась и не защищалась, я как будто и сама хотела быть жертвой домашнего насилия."
    n 1t "Всё это продолжалось, пока [player] об этом не узнал, и он пошёл со мной и помог защитить меня."
    show natsuki at t32 zorder 3
    show sayori 2h at f33 zorder 4
    s "Так вот почему на твоём теле было так много синяков..."
    s 1h "Мне жаль это слышать, Нацуки."
    show sayori 1g at t33 zorder 3
    show natsuki 5d at f32 zorder 4
    n "Да не парься так."
    n 1c "И к тому же, случай Юри намного хуже моего, потому что папа хотя бы перестал меня бить."
    n 1d "Но спасибо тебе, [player]."
    show yuri 1s at t31 zorder 2
    n "Мы с отцом постепенно налаживаем отношения с того дня, и должна сказать, у нас пока неплохо получается!"
    show natsuki 1a at t32 zorder 3
    mc "Я просто сделал то, что должен был, но я рад, что всё закончилось вот так."
    show sayori 2l at f33 zorder 4
    s "Кажется, моя очередь говорить..."
    s 1k "Итак, видите ли..."
    s 1h "У меня тоже довольно серьёзная проблема в моей жизни."
    show yuri 1zg at t31 zorder 2
    show natsuki 1za at t32 zorder 3
    s "Юри и [player] уже и так знают."
    s 1k "Я..."
    s 2h "Я страдаю депрессией почти всю свою жизнь."
    show sayori 2g at t33 zorder 3
    show natsuki 1p at f32 zorder 4
    n "Д-депрессия?! ТЫ?! ИЗ ВСЕХ ЛЮДЕЙ?!!"
    show natsuki at t32 zorder 3
    show sayori 2h at f33 zorder 4
    s "Я знаю... Должно быть, достаточно шокирующе для вас."
    s "Вы всегда видели только улыбку и счастье, но почти всё время это было совсем не то, что я чувствовала на самом деле."
    s 1h "Всё, что я чувствовала, это тоска, уныние и бесполезность, вплоть до того момента, когда я..."
    s 2v "Когда я хотела покончить с собой."
    show sayori at t33 zorder 3
    show yuri 2p at f31 zorder 4
    y "Ч-чего?!"
    y "[persistent.sayoriname], ты не рассказывала об этом раньше!"
    show yuri 2n at t31 zorder 3
    show sayori 4v at f33 zorder 4
    s "Мне очень жаль, но я просто не могла!"
    s 1zd "Но вам переживать не нужно, [player] остановил меня, прежде чем я смогла что-то с собой сделать."
    s 2zc "Он показал мне, что он на самом деле заботится обо мне, и что вы все тоже заботитесь."
    show yuri 1s at t31 zorder 3
    show natsuki 1m at t32 zorder 2
    s 1zc "Всё, чего я хотела, это чтобы все были счастливы, и если забота обо мне помогает вам себя чувствовать это, тогда я продолжу."
    s "Я просто хочу сказать спасибо огромное вам всем, я думала, вы будете не готовы."
    show sayori 1d at t33 zorder 3
    show yuri 2v at f31 zorder 4
    y "Я до сих пор слегка нервничаю, теперь когда все знают, что я с собой делаю."
    y 1zi "Но я вам доверяю, поэтому и согласилась."
    show yuri 1s at t31 zorder 2
    show natsuki 5y at f32 zorder 4
    n "Честно говоря, я даже с каким-то нетерпением ждала, чтобы всё вам рассказать."
    n 1t "Думаю, теперь вы должны понять, почему я храню мангу в клубной комнате."
    n 2k "Но есть что-то, что я хочу знать..."
    n "Моника, почему за весь наш импровизированный сеанс психотерапии ты не сказала ни слова?"
    show yuri at t41 zorder 1
    show natsuki 1za at t42 zorder 2
    show sayori 1b at t43 zorder 3
    show monika 1p at f44 zorder 4
    m "Я..."
    m 1o "..."
    show monika at t44 zorder 3
    show sayori 2c at f43 zorder 4
    s "Хочешь сказать нам о том, что тебя беспокоит?"
    show sayori 2b at t43 zorder 3
    show monika 1p at f44 zorder 4
    m "Н-нет... Я ещё н-не готова к этому..."
    show monika 1o at t44 zorder 3
    show sayori 1zc at f43 zorder 4
    s "Всё в порядке, не торопись."
    s 2zc "Тогда скажи, когда будешь готова."
    show sayori 1d at t43 zorder 3
    show yuri 2f at f41 zorder 4
    y "А что насчёт тебя, [player]?"
    y "У тебя тоже какие-то проблемы наподобие наших?"
    show yuri 2e at t41 zorder 1
    show sayori 1b at t43 zorder 3
    mc "Нет, у меня нет никаких серьёзных проблем, по крайней мере, не таких, через которые проходите вы."
    mc "Но было время, когда я чувствовал только гнев и ненависть, и я был совсем другим человеком, не таким, каким вы видите меня сейчас."
    show sayori 1g at t43 zorder 4
    show yuri 1zg at t41 zorder 1
    show natsuki 1n at t42 zorder 2
    show monika 1g at t44 zorder 3
    mc "Я отклонял любую помощь и был совсем один-одинёшенек в течение очень долгого времени..."
    mc "И даже до этого почти никто не уважал меня."
    mc "У меня всё ещё были и есть друзья из моего мира, но несмотря на это, я ничего не мог с собой поделать, и не чувствовал ничего, кроме жажды мести."
    mc "Месть на тех, кто и заставлял меня чувствовать себя таким..."
    show yuri 2t at f41 zorder 4
    y "Звучит так, как будто это совсем не серьёзно."
    show yuri at t41 zorder 1
    mc "Это было серьёзно, но сейчас я в порядке."
    mc "Я больше так себя не чувствую, и я больше не хочу отомстить им."
    show sayori 2zc at f43 zorder 4
    s "Хорошо, но поговори со мной, когда это ощущение опять возникнет."
    s 1zc "Я тоже хочу что-то для тебя сделать."
    show sayori 1d at t43 zorder 3
    show monika 1f at t44 zorder 4
    show yuri 1s at t41 zorder 1
    mc "Хорошо, я понимаю."
    mc "Но я правда в порядке. Если бы я чувствовал себя хуже, я бы серьёзно колебался, прежде чем рассказывать вам."
    mc "Сейчас {b}ты{/b} – та, у которой трудная жизненная ситуация..."
    show sayori 1h at f43 zorder 3
    s "Да, я знаю."
    s 2zc "Но я уже планирую назначить себе психотерапевта."
    show sayori 1d at t43 zorder 3
    show natsuki 2k at f42 zorder 4
    n "Я только хотела об этом спросить."
    n 2m "Но ты уверена, что об этом стоит говорить с другими?"
    show natsuki 2n at t42 zorder 2
    show sayori 2zc at f43 zorder 4
    s "[player] всегда будет со мной, поэтому я точно уверена."
    show sayori 2d at t43 zorder 3
    show yuri 2zi at f41 zorder 4
    y "Я же вижу, что он действительно заботится о тебе, раз уж он так хочет пойти с тобой."
    show yuri 2s at t41 zorder 1
    show sayori 4zc at f43 zorder 4
    s "Поэтому я и люблю его."
    show monika 1z at t44 zorder 3
    show natsuki 1a at t42 zorder 2
    s 1l "И, кажется, для всех это уже совсем не удивительно."
    show sayori 1y at t43 zorder 4
    mc "Уже нет никакого смысла скрывать."
    show sayori 1d at t43 zorder 4
    mc "Нравится людям это или нет, нас это волновать не должно."
    mc "Мы здесь друг для друга – вот что на самом деле важно."
    mc "Кем мы себя видим – вот, что должно нас на самом деле волновать."
    show sayori 1zc at f43 zorder 4
    s "Да, ты прав."
    scene bg black with dissolve_scene_full
    "[persistent.sayoriname] подходит и прижимается ко мне."
    "И мы впервые... целуемся."
    "Сперва я думал, что это просто лишнее, глупое, ненужное."
    "Но [persistent.sayoriname] заставляет меня чувствовать себя по-другому, она и впрямь замечательна."
    "Мы прекращаем поцелуй, и пока это происходит, я замечаю гнев Моники."
    scene bg living_room with dissolve_scene_full
    show yuri 1c at t41 zorder 1
    show natsuki 5a at t42 zorder 2
    show sayori 4d at t43 zorder 3
    show monika 1za at f44 zorder 4
    m "..."
    m 1zb "Я больше не могу на это смотреть!"
    show yuri 1e at t31 zorder 1
    show natsuki 1za at t32 zorder 2
    show sayori 1b at t33 zorder 3
    show monika at thide zorder 4
    hide monika
    "И прежде чем кто-то успевает обработать хоть что-то, Моника уже выбегает из дома [persistent.sayoriname]."
    show sayori 2h at f33 zorder 4
    s "Ч-что произошло? Почему Моника ушла?"
    show sayori 2g at t33 zorder 3
    show natsuki 1k at f32 zorder 4
    n "И что она имела в виду, когда сказала «Я больше не могу на это смотреть»?"
    show natsuki 1za at t32 zorder 3
    show yuri 2t at f31 zorder 4
    y "Быть может, это потому, что она... ревнует?"
    show yuri at t31 zorder 3
    show natsuki 1m at t32 zorder 2
    show sayori 1h at f33 zorder 4
    s "Н-но, к-кажется, она не была против ранее..."
    show sayori 1g at t33 zorder 4
    mc "..."
    mc "Как думаешь, почему тогда она так загрустила?"
    mc "Всё потому что я люблю тебя, а не её."
    mc "В этом и кроется вся причина, почему она вела себя так неестественно."
    show sayori 4v at f33 zorder 4
    s "Н-нет..."
    s "Почему так? Почему она вообще такая?"
    show sayori at t33 zorder 3
    mc "Кто-угодно сможет быть таким, даже те, которые, по твоему мнению, наименее подвержены этому."
    mc "Я пытался помочь всё это время, но кажется, ей становилось только хуже."
    show yuri 1t at f31 zorder 4
    y "Что мы можем сделать, чтобы помочь ей?"
    show yuri 1zg at t31 zorder 4
    mc "Что-угодно, но только не пытаться разлучить нас с [persistent.sayoriname]."
    mc "Она должна научиться отпустить это, даже если это и очень сложно."
    show yuri 2q at f31 zorder 4
    y "Естественно, вы двое должны продолжать ваши отношения, даже несмотря на всё это."
    y 2t "Я спрашиваю, чем {i}ещё{/i} мы можем помочь?"
    show yuri 1zg at t31 zorder 3
    mc "Я не уверен... Это, по сути, что-то, с чем человек должен справиться сам."
    mc "И если она достаточно сильная, тогда рано или поздно она это превозможет."
    mc "Я верю, что она справится."
    show sayori 2zd at f33 zorder 4
    s "Да, она президент Литературного клуба, как-никак."
    s "Она и так уже много сделала, и лучше у неё уже не получится."
    show sayori 2t at t33 zorder 3
    show natsuki 5a at t32 zorder 2
    show yuri 2zi at f31 zorder 4
    y "Ты права! Она всегда уверена в себе и всегда упорно трудится."
    y 2t "Но я всё ещё хочу ей чем-то помочь."
    show yuri at t31 zorder 4
    mc "Быть может, ты сможешь сделать то, что у тебя получается лучше всего."
    mc "И под этим я подразумеваю... сделать чаю."
    mc "Кто знает, может, чай поможет ей успокоится, зная, что мы все о ней заботимся."
    show yuri 1zi at f31 zorder 4
    y "Полагаю, я смогу это сделать."
    y 1d "Что-угодно, чтобы мои друзья чувствовали себя лучше."
    show yuri 1a at t31 zorder 3
    mc "Ну а кроме этого..."
    mc "Есть ли что-то ещё в твоих планах?"
    show sayori 2r at f33 zorder 4
    s "Нет, это всё!"
    s 1k "Но я и правда не ожидала, что всё развернётся... вот так."
    s 2c "Не пойми меня неправильно, стало намного лучше после того, как мы проговорили проблемы друг друга, ну и наш первый поцелуй."
    s 1k "Но, кажется, даже до того, как Моника ушла, она и так уже была сильно расстроена чем-то..."
    show sayori at t33 zorder 3
    mc "Я уверен, что всё наладится к завтрашнему дню, мы просто должны дать ей время."
    show natsuki 1c at f32 zorder 4
    n "Ладно, я могу более-менее понять."
    n "Я тоже злюсь время от времени, в основном потому что Моника постоянно переносит мою мангу."
    n 5c "Так что, кажется, я понимаю, что это такое... но в случае с ревностью это намного хуже."
    show natsuki 5za at t32 zorder 2
    show yuri 2b at f31 zorder 4
    y "Я попытаюсь поднять ей настроение завтра, но сегодня я уже должна уходить."
    show sayori 1d at t33 zorder 3
    y 1b "Спасибо за приглашение, я чувствую себя чуть лучше и чуть более облегчённой после того, как я всё рассказала."
    show yuri 1a at t31 zorder 4
    mc "Тогда, думаю, увидимся завтра!"
    show yuri at thide zorder 4
    hide yuri
    show natsuki at thide zorder 2
    hide natsuki
    "Юри и Нацуки махают нам и уходят."
    show sayori 1a at t11 zorder 4
    mc "Ладно... Должен сказать, я этого вообще не ожидал."
    mc "Как Юри и Нацуки вообще согласились на это?!."
    show sayori 2c at f11 zorder 4
    s "Я думала, что они откажутся, но я удивилась, когда они согласились."
    s 2zc "И теперь я чувствую себя намного радостнее после того, как мы все всё сказали."
    show sayori 2d at t11 zorder 4
    mc "Это касается нас обоих."
    mc "Время проходит слишком быстро, ещё недавно я только обещал, что никогда не покину и не брошу тебя."
    mc "А сейчас мы здесь, тебе становится лучше, Юри становится лучше, и мы все знаем проблемы друг друга."
    show sayori 1zc at f11 zorder 4
    s "Это всё стало возможным только благодаря тебе, [player]."
    show sayori 1d at t11 zorder 4
    mc "Не буду лукавить, я действительно сделал это возможным."
    mc "Но ничего из этого не было бы без тебя, кто знает, насколько плохо дела были бы, если бы ты не решила продолжить."
    show sayori 2zc at f11 zorder 4
    s "Ты прав насчёт того, что ты сказал."
    s 1h "Мне стоило послушать тебя раньше, мне так жаль..."
    show sayori 1g at t11 zorder 4
    mc "Не стоит."
    mc "Депрессия затмевала твоё восприятие и твоё мнение, и я это понимаю."
    mc "Но что важно, так это то, что я сумел вытащить тебя из этой ямы."
    mc "Но помни, что это не было бы возможно, если бы ты не была такой сильной духом, как сейчас."
    show sayori 2zc at f11 zorder 4
    s "Да, может, я действительно сильнее духом, чем мне кажется."
    s 2b "..."
    s 1c "[player], у меня есть идея."
    s 1zc "Может, сходишь и утешишь Монику? Она, скорее всего, обрадуется."
    show sayori 1d at t11 zorder 4
    mc "Да, ты права."
    mc "Может, это именно то, что она хочет..."
    mc "Скоро буду!"
    scene bg house2 with dissolve_scene_full
    stop music fadeout 5.0
    "Я звоню в дверной звонок."
    "..."
    "Нет ответа."
    mc "Моника?"
    mc "Она не дома? Если всё-таки нет... куда она, блин, пропала?"
    scene bg black with dissolve_scene_full
    "А в это время..."
    scene bg living_room with dissolve_scene_full
    "Моника возвращается в дом [persistent.sayoriname]."
    show sayori 2bc at f11 zorder 4
    s "[player]? Ты уже вернулся?"
    show monika 1bza at t22 zorder 3
    show sayori 2bn at f21 zorder 4
    s "М-Моника?! А что ты здесь делаешь?"
    show sayori at t21 zorder 3
    show monika 1bzb at f22 zorder 4
    m "Я тебя ненавижу... Я ненавижу тебя ВСЕЙ ДУШОЙ!"
    show monika 1bzc at t22 zorder 3
    show sayori 1bv at f21 zorder 4
    s "Ч-чего?"
    s "Моника, о чём ты говоришь?"
    show sayori at t21 zorder 3
    show monika 1bzb at f22 zorder 4
    m "Ты украла {b}его{/b} у меня! {b}Он{/b} проводит всё время с тобой!"
    show monika 1bzc at t22 zorder 3
    show sayori 2bh at f21 zorder 4
    s "Н-но [player] любит меня..."
    show sayori 2bg at t21 zorder 3
    show monika 1bza at f22 zorder 4
    m "Вот в этом-то и проблема."
    m 1bzb "Хватит путаться у него под ногами! Он бы прожил гораздо лучшую жизнь без тебя!"
    m "А ты только делаешь ему хуже со своей депрессией!"
    show sayori 1bv at t21 zorder 3
    m "Поэтому прекрати с ним разговаривать и дай ему уйти!"
    show monika 1bzc at t22 zorder 3
    show sayori at f21 zorder 4
    s "{w=0.25}.{w=0.25}.{w=0.25}."
    s 1bi "..."
    s 1bj "А вот тут ты неправа."
    s "[player] сделал так много, чтобы помочь мне, и ты даже не представляешь, через что ему пришлось пройти!"
    s 4bj "Он на самом деле любит меня, а я люблю его!"
    s 1bj "И даже если у меня депрессия, он совершенно не против, я чётко это знаю."
    s "И я тоже хочу что-то для него сделать."
    s "И если это значит, что мне придётся его защищать, то тогда я его защищу!"
    show sayori 1bi at t21 zorder 3
    show monika 1bza at f22 zorder 4
    m "Ах! Если бы я только..."
    m "..."
    m 1bzb "Но уже слишком поздно, и кажется, мне нужно разобраться с тобой по-плохому..."
    show monika at thide zorder 4
    hide monika
    show sayori 1bg at t21 zorder 4
    "Моника быстро выбегает из дома [persistent.sayoriname]."
    scene bg house2 with dissolve_scene_full
    mc "..."
    mc "Её дом – это единственное место, куда, как я думаю, она смогла бы убежать..."
    mc "Мне нужно возвращаться обратно к [persistent.sayoriname], иначе я просто хожу кругами."
    scene bg residential_day with dissolve_scene_full
    "Пока я возвращаюсь, Моника пробегает мимо меня и не говорит ни слова."
    mc "Моника? А что..."
    "..."
    "А что происходит?"
    "Кажется, она плакала, неужели кто-то что-то с ней сделал?"
    "Но... кто?"
    "Минуточку... Неужели это именно то, о чём я думаю?"
    "Она выбегала из направления дома [persistent.sayoriname]."
    "Нужно возвращаться сейчас же."
    scene bg living_room with dissolve_scene_full
    show sayori 1bg at t11 zorder 4
    mc "[persistent.sayoriname]!"
    mc "Тут случайно не пробегала Моника?"
    show sayori 2bh at f11 zorder 4
    play music t10
    s "Да, пробегала."
    s "И она сказала мне всякие жестокости."
    s 2bzc "Но не переживай, я ответила ей, когда она мне сказала, что мол мне лучше не попадаться у неё на пути."
    show sayori 2bd at t11 zorder 4
    mc "Что она тебе сказала?!"
    mc "Ну уж нет, этого я так просто не оставлю."
    show sayori 1bh at f11 zorder 4
    s "Нет, всё в порядке, правда."
    s 1bzc "Моника и правда ревнует, и в ней говорит это чувство, а не она сама."
    show sayori 1bd at t11 zorder 4
    mc "И то верно, но она должна дважды подумать, прежде чем говорить что-то подобное."
    mc "Я задам ей парочку вопросов завтра."
    mc "Тебе не стоит ни о чём переживать, давай лучше во что-то поиграем, чтобы забыть обо всей этой ситуации."
    show sayori 2bzc at f11 zorder 4
    s "Да, звучит здорово."
    scene bg black with dissolve_scene_full
    "Мы проводим ещё больше времени вместе, чтобы забыть о произошедшем, пока не наступила поздняя ночь."
    "Чувства не могут описать того, как же я хочу наказать Монику, но в то же время я не хочу быть слишком жестоким."
    "После того, как мы поели и сходили в школу, и после долгих и скучных часов уроков мы наконец-то собираемся встретиться в клубе."
    scene bg corridor with dissolve_scene_full
    show sayori 1k at t11 zorder 4
    mc "Нервничаешь?"
    show sayori 2h at f11 zorder 4
    s "А как я могу не нервничать?"
    s 1h "Моника – мой друг, и услышать все эти гадости именно от неё – это больно."
    s "Но я всё ещё хочу ей помочь, даже если она не хочет, чтобы я тебя любила."
    show sayori 1g at t11 zorder 4
    mc "Это просто твоя личность, [persistent.sayoriname]."
    mc "И я уверен, мы сможем придумать решение."
    show sayori 1zc at f11 zorder 4
    s "Да, было бы здорово..."
    show sayori 1b at t11 zorder 4
    "Вдруг как гром среди ясного неба, Юри выбегает из клубной комнаты и бежит в нашу сторону."
    stop music fadeout 5.9
    show sayori at t22 zorder 3
    show yuri 2n at f21 zorder 4
    y "Р-ребята! П-пожалуйста, быстрее, идём с н-нами!"
    y "Вы должны это увидеть!"
    show yuri at t21 zorder 3
    show sayori 2h at f22 zorder 4
    s "Ч-что происходит?"
    scene bg black with dissolve_scene_full
    "Юри тащит нас обоих обратно в клубную комнату, и то, что мы там увидели, поразило нас до глубины души."
    scene bg club_day with dissolve_scene_full
    mc "Что за хрень?!"
    mc "И почему парта Моники выцарапана и перевёрнута вверх тормашками?!"
    mc "И что со всеми этими бумагами?!"
    show sayori 1z at t31 zorder 3
    show yuri 1n at f32 zorder 4
    show natsuki 5u at t33 zorder 2
    y "Мы без понятия, что здесь произошло."
    y "Сама Моника тоже отсутствует, но я думаю, это что-то, связанное с ней самой."
    show yuri at t32 zorder 4
    mc "А, ну кстати... она же плакала вчера."
    mc "Мы должны отыскать её, сейчас же."
    mc "Все за мной."
    scene bg black with dissolve_scene_full
    pause(0.5)
    play sound Glow
    "Я усиливаю внимание, чтобы попытаться найти её."
    "Она стоит снаружи школы, и мы все бежим к ней."
    scene bg residential_day with dissolve_scene_full
    show monika 1zc at t11 zorder 4
    mc "Моника! Вот ты где!"
    mc "Что произошло с клубной комнатой?! И почему ты здесь?"
    show sayori 1v at f41 zorder 4
    show monika at t44 zorder 3
    show yuri 1t at t42 zorder 2
    show natsuki 1i at t43 zorder 1
    s "Моника? Ты в порядке?"
    show sayori at t41 zorder 3
    show monika 1zb at f44 zorder 4
    m "{cps=*0.5}ЖИВО ЗАТКНУЛИСЬ ВСЕ БЛЯТЬ!{/cps}"
    m "С меня довольно, я так больше не могу!"
    m 1x "[player], прости за то, что я сейчас сделаю."
    show monika 1w at t44 zorder 4
    "Инстинктивно я принимаю защитную стойку."
    show sayori 4w at h41 zorder 3
    show yuri 3p at h42 zorder 2
    show natsuki 1p at h43 zorder 1
    play sound "sfx/fire2.ogg"
    mc "Ты ничего мне не сделаешь."
    mc "Что бы ты ни делала, это не сработает, поэтому прекрати эту ересь."
    show monika 1x at f44 zorder 4
    m "Я знаю, что я не могу одолеть тебя."
    m 3za "И вот поэтому я должна буду сделать это."
    play sound "sfx/glitch1.ogg"
    show screen tear(30, 0.05, 0.05, -20, 80)
    pause(1.2)
    hide screen tear
    scene bg black
    pause(5.0)
    mc "Что?"
    mc "..."
    mc "Где я, блин, вообще?!"
    show monika 1e at t11 zorder 4
    mc "Что ты сделала?!"
    show monika 1y at f11 zorder 4
    m "Это не важно."
    m "Важно то, что мы вместе, и никто не встанет на нашем пути."
    show monika 1e at t11 zorder 4
    mc "Нет, это невозможно."
    mc "Где они?!"
    show monika 1x at f11 zorder 4
    m "Перестань заботиться о них."
    m "Я пожертвовала почти всеми своими способностями, чтобы сделать это..."
    m "Теперь я ничего не смогу сделать, и я это сделала ради тебя..."
    show monika 1w at t11 zorder 4
    mc "..."
    mc "Значит, это всё было зря."
    mc "Потому что я найду и отыщу их, вне зависимости от того, чего мне это будет стоить."
    mc "Они должны быть где-то, и ты не остановишь меня от того, чтобы отыскать их."
    show monika 1x at f11 zorder 4
    m "[player]! Нет!"
    m "{cps=30}Пожалуйста, останься рядом со м-{/cps}{nw}"
    play sound "sfx/glitch1.ogg"
    show screen tear(30, 0.05, 0.05, -20, 80)
    pause(1.2)
    hide screen tear
    pause(0.01)
    scene bg black
    pause(3.5)
    "Я чувствую их присутствие в этой бесконечной пустоте."
    "Я заметно облегчился, когда я знаю, что они рядом..."
    "Без задней мысли, я быстро приближаюсь к тому самому месту."
    scene bg black with dissolve_scene_full
    show sayori 4w at f31 zorder 4
    show yuri 1p at t32 zorder 3
    show natsuki 1p at t33 zorder 2
    s "[player]?! Что произошло?! И где мы вообще?!"
    show sayori at t31 zorder 3
    mc "Я и сам в замешательстве, но вот что я теперь могу сказать вам."
    mc "Именно Моника была тем самым человеком, который хотел вам навредить, с немного другими способностями, не такими, как у меня."
    mc "Она пыталась вам навредить всё это время, но безрезультатно, потому что я блокировал все её плохие намерения."
    mc "Но сейчас она сделала что-то очень мощное взамен на все свои силы, чтобы превратить этот мир в какую-то другую реальность."
    show yuri 2p at f32 zorder 4
    y "У-у М-Моники тоже были способности?!"
    y "Я думала, что ты единственный среди нас!"
    show yuri at t32 zorder 3
    mc "К сожалению, нет."
    mc "Она в состоянии изменять этот мир... ну, или скорее... была в состоянии."
    show natsuki at f33 zorder 4
    n "Почему ты нам ничего не сказал?!"
    show natsuki at t33 zorder 2
    mc "А что я должен был сказать? «У вашего друга есть сверхъестественные силы, которые буквально смогли бы изменить всю вашу реальность»?"
    mc "Я ни капли не сомневаюсь, что она бы сделала то же самое вне зависимости от этого."
    mc "А так был хотя бы маленький шанс, что она этого не сделает, если бы я сохранил это в тайне ото всех."
    show sayori 1v at t31 zorder 3
    show yuri 2t at t32 zorder 2
    show natsuki 1m at f33 zorder 4
    n "..."
    n 5m "Ну да, ты прав..."
    n 1m "Но что нам теперь делать?"
    n "Как нам выбраться из этого места?"
    show natsuki at t33 zorder 1
    mc "{w=0.5}.{w=0.5}.{w=0.5}."
    window hide
    pause(2.0)
    "Я тщательно обдумываю сложившуюся ситуацию."
    "Мы не можем просто стоять тут целую вечность..."
    "Хотя постойте... Так вот же оно!"
    play music Hope1
    mc "Помните, как я сказал вам, что с достаточной силой воли можно добиться буквально всего?"
    mc "Кажется, настал тот самый момент. У нас просто нет другого выхода..."
    show yuri 1t at f32 zorder 4
    y "Н-но к-как?"
    show yuri at t32 zorder 2
    mc "Мы должны сопротивляться."
    mc "Никто из нас не хочет быть взаперти, но для этого нам нужно направить свою внутреннюю силу."
    mc "Пожалуйста... держитесь крепче и не отпускайте..."
    show sayori 1t at f31 zorder 4
    s "..."
    s 2zd "Я верю тебе и тому, что ты делаешь, [player]."
    show sayori 1t at t31 zorder 3
    show yuri 2zi at f32 zorder 4
    y "Я тоже тебе верю, и я сделаю всё возможное, чтобы вернуться."
    show yuri 2s at t32 zorder 2
    show natsuki 4d at f33 zorder 4
    n "Да, можешь на меня рассчитывать!"
    show natsuki 4a at t33 zorder 1
    mc "Раз уж мы все готовы, тогда мы не должны терять время впустую."
    mc "Я верю, что мы сможем сразиться против этого мира вместе и заставить его вернуться."
    show yuri 3w at t32 zorder 2
    show sayori 4ze at t31 zorder 3
    show natsuki 1zc at t33 zorder 1
    stop music fadeout 5.0
    mc "В вас есть всё, чтобы противотоять злым деяниям Моники."
    mc "Это для тебя, для нас, для всех вместе..."
    mc "Так что пожалуйста... Не сдавайтесь и боритесь внутри."
    mc "Потому что у нас друг в друге есть всё, чтобы этому противостоять."
    mc "Именно воля к сопротивлению заставляет нас идти дальше и даёт надежду."
    mc "И я верю, что у каждого из вас есть хотя бы малая её часть..."
    play music Hope2
    pause(2.0)
    scene white with dissolve_scene_full
    pause(1.0)
    scene white with dissolve_scene_full
    pause(1.0)
    scene bg black with dissolve_scene_full
    show natsuki 1zc at t11 zorder 1
    mc "Нацуки... ты очень храбрая и сильная за то, что ответила своему отцу."
    mc "Я очень тобой горжусь..."
    scene bg black with dissolve_scene_full
    show yuri 3w at t11 zorder 2
    mc "Ты всегда была способной на то, чтобы остановить самоповреждения, Юри."
    mc "И я очень рад, что ты стараешься, даже если ты это делаешь только ради меня."
    scene bg black with dissolve_scene_full
    show sayori 4ze at t11 zorder 3
    mc "[persistent.sayoriname]..."
    mc "Ты была очень способной сопротивиться депрессии..."
    mc "За всё, что ты для меня сделала, что-то, чего никогда и никому доселе не удавалось."
    mc "Я люблю тебя..."
    stop music fadeout 3.0
    scene bg black with dissolve_scene_full
    play sound Hope3
    pause(1.5)
    "Спасибо вам всем."
    "Спасибо за то, что были со мной и уважали меня за то, кто я есть."
    "И за то, что дали всем шанс исправить всё."
    scene bg black with dissolve_scene_full
    pause(2.0) #End of Chapter 4: Resistance #######################################################################################################################################
    scene bg Chapter5 with dissolve_scene_full
    pause(3.0)
    scene bg black with dissolve_scene_full
    pause(5.0)
    scene bg residential_day with dissolve_scene_full
    pause(1.0)
    show sayori 1ze at t31 zorder 3
    show yuri 3w at t32 zorder 2
    show natsuki 1zc at t33 zorder 1
    pause(1.0)
    show sayori 1n at f31 zorder 4
    s "..."
    s 1m "М-мы вернулись!"
    show yuri 1f at t32 zorder 3
    show natsuki 1c at t33 zorder 2
    s 4zd "Мы вернулись!"
    show sayori at t31 zorder 3
    show yuri 1d at t32 zorder 2
    show natsuki 4z at f33 zorder 1
    n "Да! Действительно вернулись!"
    n 1k "Но у меня до сих пор темно в глазах."
    show natsuki at t33 zorder 1
    mc "Что важно, так это то, что этот мир вернул нас."
    mc "Я очень горжусь всеми вами, вы все большие молодцы."
    show sayori 1b at t41 zorder 3
    show yuri 1e at t42 zorder 2
    show natsuki 5f at t43 zorder 1
    show monika 1s at f44 zorder 4
    m "Н-н-н-нет..."
    m "Н-невозможно."
    m "К-как вы смогли вернуться?!"
    show monika at t44 zorder 4
    mc "Даже невозможное возможно, если ты просто очень постараешься и приложишь все свои усилия."
    mc "Это что-то, что тебе никогда не понять, в отличие от них."
    mc "Вот поэтому мы смогли вернуться, и на сей раз... это навсегда."
    show monika at s44 zorder 4
    "Моника валится на землю, будучи побеждённой на самом деле, поскольку её жертва насегда останется впустую."
    m 1x "Это всё, что у меня было... И я отдала всё тебе."
    show sayori 1g at t41 zorder 3
    show yuri 1zg at t42 zorder 2
    m 1z "Теперь я действительно бесполезна..."
    "Эти слова внезапно меняют моё настроение, и теперь я чувствую гнев."
    show natsuki 1p at f43 zorder 4
    n "Бесполезна?!"
    n 1o "Да ты хотела нас всех убить! Ты же не человек, ты зверь!!"
    show natsuki at t43 zorder 1
    show yuri 2t at f42 zorder 4
    y "Нацуки, пожалуйста... Успокойся."
    y "Моника, должно быть, и так ужасно себя чувствует, она сделала это только из-за того, что на неё набросилось."
    show yuri at t42 zorder 2
    show natsuki 5e at f43 zorder 4
    n "Это её не извиняет!"
    show natsuki 5f at t43 zorder 1
    show yuri at f42 zorder 4
    y "Конечно, не извиняет, но что хорошего в мести?"
    y "Она больше ничего не сможет сделать, и она и так уже изрядно наказана за все свои злодеяния."
    show natsuki 1e at f43 zorder 4
    show yuri at t42 zorder 2
    n "Ну что же, а я вот так не думаю!"
    n "Я хочу, чтобы её наказали, это моё последнее слово."
    show natsuki 1g at t43 zorder 1
    show yuri 1v at f42 zorder 4
    y "Я хочу простить её и дать ей шанс искупить свои грехи."
    show monika 1x at t44 zorder 3
    y 1zi "Если я смогла измениться, то сможет и она."
    show yuri 1s at t42 zorder 2
    show sayori 1d at f41 zorder 4
    s "..."
    s 2zc "Последнее слово за тобой, [player]."
    s 1zc "Ты знаешь, что для нас правильно, поэтому пожалуйста, прими решение и за меня тоже."
    show sayori 1d at t41 zorder 3
    menu:
        "..."
        "Наказать её":
            $ value = 16
        "Простить её":
            $ value = 17
    if value == 16:
        mc "{w=0.25}.{w=0.25}.{w=0.25}."
        "Гнев стремительно усиливается..."
        "Почти как будто бы я уже чувствовал это раньше."
        "Я чувствую..."
        "Я чувствую{w=0.25}.{w=0.25}.{w=0.25}. беспомощность,{w=0.5} я чувствую месть."
        "Я{w=0.25}.{w=0.25}.{w=0.25}. чувствую{w=0.25}.{w=0.25}.{w=0.25}. {w=0.05}н{w=0.05}е{w=0.05}н{w=0.05}а{w=0.05}в{w=0.05}и{w=0.05}с{w=0.05}т{w=0.05}ь{w=0.05}."
        window hide
        pause(2.5)
        play music hb
        show layer master at heartbeat
        show veinmaskb zorder 5: #Aggression scene start
            alpha 1.0
        show veins onlayer front:
            additive 1.0
            alpha 0.5
        mc "НЕТ ТЕБЕ ПРОЩЕНИЯ, ТЫ ЖЕСТОКИЙ, САМОВЛЮБЛЁННЫЙ МОНСТР."
        show sayori 4w at t41 zorder 3
        show yuri 3p at t42 zorder 2
        show natsuki 1zb at t43 zorder 1
        show monika 1s at t44 zorder 4
        mc "ЗА ТО, ЧТО ТЫ СДЕЛАЛА, ТЕБЕ НЕТ ПРОЩЕНЬЯ."
        mc "И ТЫ ОТСЮДА НЕ ВЫБЕРЕШЬСЯ, ТЫ БУДЕШЬ СТРАДАТЬ."
        mc "Я ПОКАЖУ ТЕБЕ, ЧТО ТАКОЕ НАСТОЯЩАЯ БОЛЬ."
        mc "Я УСТАЛ ОТ ВСЕГО ЭТОГО, И ПОСЛЕ ВСЕГО, ЧТО МЫ ДЛЯ ТЕБЯ СДЕЛАЛИ, ТЫ ДО СИХ ПОР ХОЧЕШЬ СДЕЛАТЬ ИМ БОЛЬНО."
        mc "И ЕСЛИ ТЫ ДУМАЕШЬ, ЧТО ТЫ ПОСЛЕ ВСЕГО ЭТОГО ВЫБЕРЕШЬСЯ, ТО ТЫ ОХРЕНЕТЬ КАК НЕПРАВА."
        mc "ТЫ НЕ СКРОЕШЬСЯ ОТ МЕНЯ, И Я УВЕРЯЮ, ЧТО ТЫ ОЧЕНЬ НЕЛЕГКО ОТДЕЛАЕШЬСЯ."
        if persistent.brutality == True:
            mc "Я ДАМ ТЕБЕ НАИХУДШИЙ КОШМАР, КОТОРЫЙ ТЫ ТОЛЬКО СМОЖЕШЬ СЕБЕ ПРЕДСТАВИТЬ."
        show sayori at f41 zorder 4
        s "[player]!! НЕТ!!"
        s "Пожалуйста! Это не настоящий ты!!"
        s "Пожалуйста, прекрати это!!"
        show sayori at t41 zorder 4
        "Но я уже слишком разошёлся в плане ненависти, чтобы вот так просто остановить это..."
        mc "ОНА ЦЕЛИКОМ И ПОЛНОСТЬЮ ЗАСЛУЖИВАЕТ НАКАЗАНИЯ."
        mc "ПРИМИ ЭТО И ПОДЧИНИСЬ СВОЕМУ ПРАВОСУДИЮ."
        mc "ТЫ НЕ СМОЖЕШЬ ОСТАНОВИТЬ МЕНЯ ОТ ТОГО, ЧТОБЫ Я ПРИЧИНЯЛ ТЕБЕ ЭТО."
        if persistent.brutality == True:
            mc "КАЖДЫЙ, КТО ХОТЬ РАЗ ВИДЕЛ МЕНЯ И ТО, НА ЧТО Я СПОСОБЕН, И ТАК ЗНАЮТ."
            mc "МЕНЯ СТРАШАТСЯ НЕ ПРОСТО ТАК."
        mc "ЖИЗНЬ МЕНЯ НЕ ОГРАНИЧИВАЕТ."
        mc "СМЕРТЬ МЕНЯ НЕ ОСТАНОВИТ."
        $ style.say_dialogue = style.edited
        mc "{cps=20}Я ЕСТЬ БОГ{/cps}."
        mc "{cps=20}И ТЫ ЗАСЛУЖИВАЕШЬ ЛИШЬ ХУДШЕГО ИЗ ХУДШИХ ИСХОДОВ{/cps}."
        $ style.say_dialogue = style.normal
        show layer master
        stop music
        hide veinmaskb
        hide veins onlayer front
        pause(0.01)
        scene bg black
        play sound Destruction
        pause (15.0)
        mc "Ч-что..."
        mc "Нет... нет..."
        mc "Я не... Да не может этого быть!"
        mc "Это ложь, ложное воспоминание!"
        show monika 1zd at t11 zorder 4
        mc "..."
        mc "М-Моника?"
        show monika 1ze at f11 zorder 4
        m "Пожалуйста, успокойся, [player]."
        m "Всё кончено, ты переиграл и уничтожил меня."
        show monika 1zd at t11 zorder 4
        mc "Нет... это же неправда!"
        mc "И где остальные?!"
        show monika 1x at f11 zorder 4
        m "Ты уничтожил всех и вся, [player]."
        m "Мир разрушен, и я тоже ускользаю..."
        show monika 1w at t11 zorder 4
        mc "Нет... НЕТ!!"
        mc "НЕ МОЖЕТ ЭТОГО БЫТЬ! КАК Я МОГ СДЕЛАТЬ НЕЧТО ПОДОБНОЕ?!"
        show monika 1ze at f11 zorder 4
        play music still
        m "Нет, всё в порядке..."
        m "Ты был прав насчёт меня, я монстр."
        m "И я не заслуживаю ничьего прощения."
        m 1x "И после всего того, что ты и они сделали для меня, я всё ещё пыталась навредить вам."
        m "Мне так жаль..."
        show monika 1w at t11 zorder 4
        mc "Нет... Моника..."
        mc "Ты этого не заслуживаешь!"
        mc "Пожалуйста... Не уходи..."
        show monika 1ze at f11 zorder 4
        m "Я ускользаю, [player]."
        m "Но есть одно для тебя, что я смогу сделать."
        m "Я даю тебе возможность откатить всё до исходного состояния и вернуть всех."
        m 1x "Ну, кроме меня, я вернуться не смогу."
        m 1ze "Но это то, что я заслуживаю, это и есть моё наказание."
        show monika 1zd at t11 zorder 4
        mc "Нет! Есть же какой-то способ вернуть тебя!"
        show monika 1x at f11 zorder 4
        m "К сожалению, нет, уж прости меня..."
        m "Урон очень большой, и я не смогу исцелить его сама."
        m 1ze "Но обещай мне, что позаботишься об остальных, ради меня, [player]."
        m "Ты сможешь сделать всё правильно, я в тебя верю."
        m 1x "И я не хочу больше причинять никакого больше вреда, чем я уже причинила."
        m "Ведь ты для меня всё,{w=0.5} ты – моё Спасение."
        m "И я бы действительно хотела сделать для тебя что-то ещё, но у меня больше нет способностей."
        m 1ze "Так что защити их своими, чего бы это ни стоило..."
        m "{w=0.05}П{w=0.05}о{w=0.05} {w=0.05}к{w=0.05}р{w=0.05}а{w=0.05}й{w=0.05}н{w=0.05}е{w=0.05}й{w=0.05} {w=0.05}м{w=0.05}е{w=0.05}р{w=0.05}е{w=0.25}.{w=0.25}.{w=0.25}. {w=0.05}о{w=0.05}н{w=0.05}и{w=0.05} с{w=0.05}м{w=0.05}о{w=0.05}г{w=0.05}л{w=0.05}и {w=0.05}з{w=0.05}а{w=0.05}с{w=0.05}л{w=0.05}у{w=0.05}ж{w=0.05}и{w=0.05}т{w=0.05}ь{w=0.25}.{w=0.25}.{w=0.25}. {w=0.05}х{w=0.05}о{w=0.05}р{w=0.05}о{w=0.05}ш{w=0.05}у{w=0.05}ю {w=0.05}к{w=0.05}о{w=0.05}н{w=0.05}ц{w=0.05}о{w=0.05}в{w=0.05}к{w=0.05}у{w=0.25}.{w=0.25}.{w=0.25}."
        show monika 1zd at t11 zorder 4
        mc "МОНИКА!!"
        scene bg black with dissolve_scene_full
        pause(1.0)
        mc "..."
        mc "Моника..."
        mc "Спасибо тебе."
        mc "Спасибо тебе за то, что дала мне второй шанс, даже когда я этого не заслужил."
        mc "И я обещаю, что на этот раз точно всё получится, и я буду защищать их со всем, что у меня есть."
        mc "Я обязательно найду способ вернуть тебя, я клянусь..."
        mc "Я сделаю всё, что в моих силах, чтобы у тебя тоже был второй шанс, чего бы это мне ни стоило..."
        stop music fadeout 7.5
        mc "И однажды,{w=0.75} {w=0.03}м{w=0.03}ы {w=0.03}о{w=0.03}б{w=0.03}я{w=0.03}з{w=0.03}а{w=0.03}т{w=0.03}е{w=0.03}л{w=0.03}ь{w=0.03}н{w=0.03}о{w=0.03} б{w=0.03}у{w=0.03}д{w=0.03}е{w=0.03}м {w=0.03}в{w=0.03}м{w=0.03}е{w=0.03}с{w=0.03}т{w=0.03}е{w=0.03} с{w=0.03}н{w=0.03}о{w=0.03}в{w=0.03}а."
        scene bg black with dissolve_scene_full
        pause(2.0)
        $ renpy.movie_cutscene("bg/BadEnding.webm")
        jump phase10

    if value == 17:
        mc "..."
        mc "Даже после всего, что мы сделали, ты всё равно не смогла отпустить."
        mc "Но, Моника..."
        play music mend
        mc "Я прощаю тебя."
        show sayori 4zd at t41 zorder 3
        show yuri 3zi at t42 zorder 2
        show natsuki 1m at t43 zorder 1
        show monika 1x at t44 zorder 4
        mc "Ты была напугана, и тебе пришлось сражаться в одиночку."
        mc "Удерживать всех остальных в неведении всё это время."
        mc "Всё это давление заставило тебя думать, что это был единственный способ."
        mc "Должно быть, это невыносимо всё удерживать в себе настолько долго."
        mc "Поэтому я понимаю, почему ты это сделала..."
        mc "И я уверен, что вместе мы сможем что-то придумать."
        mc "Ты со мной, Моника?"
        show monika 1zd at f44 zorder 4
        m "..."
        m 1ze "Да, я с тобой."
        show monika 1zd at t44 zorder 3
        show sayori 4r at t41 zorder 3
        show yuri 1c at t42 zorder 2
        show natsuki 1a at t43 zorder 1
        "После этих слов, кажется, все взбодрились."
        "Одна долгосрочная проблема решена, ну или хотя бы мне так кажется."
        mc "Значит, я даю тебе второй шанс."
        mc "Но тебе нужно прощение и всех остальных."
        show sayori 1d at f41 zorder 4
        s "..."
        s 2zc "Я прощаю тебя, Моника."
        s "Даже если ты, скорее всего, до сих пор ненавидишь меня, я хочу дать тебе второй шанс."
        show sayori 2d at t41 zorder 3
        show monika 1x at f44 zorder 4
        m "У меня нет права ненавидеть тебя, [persistent.sayoriname]."
        m "[player] выбрал тебя, и я должна была уважить это решение."
        m "Но вместо этого я скинула весь гнев на тебя, и заставила всех думать, что ты – это и есть проблема."
        m "Прости, [persistent.sayoriname]."
        show monika 1w at t44 zorder 3
        show sayori 1zc at f41 zorder 4
        s "Всё в порядке, я тебя прощаю."
        s "И я уверена, что ты сможешь превозмочь и свою проблему тоже."
        show sayori 1d at t41 zorder 3
        show yuri 2zi at f42 zorder 4
        y "Моника, ты пригласила меня в лучший клуб, в котором я могла бы быть."
        y "И я очень благодарна тебе за это."
        y 1f "Конечно, мне очень не нравится, что ты пыталась навредить своим друзьям..."
        y 1zi "Но раз они прощают тебя, то тогда прощу и я."
        show yuri 1s at t42 zorder 2
        show natsuki 5s at f43 zorder 4
        n "..."
        n 5q "Это было очень по-детски, Моника."
        n "И я бы соврала, что после этого я не хочу ударить тебя по лицу."
        n 1m "Но они хотят простить тебя, и я не хочу ещё больше усложнять ситуацию."
        n 1t "И мне кажется, на моём месте ты бы сделала точно так же."
        n 1c "Так что я тоже тебя прощаю, но учти, что ты на очень строгом испытательном сроке."
        show natsuki 1g at t43 zorder 1
        show monika 1ze at f44 zorder 4
        m "Я обещаю, что я тебя не подведу."
        m "Спасибо всем за второй шанс..."
        m "Спасибо всем... Огромное-преогромное спасибо..."
        m 1x "Я знаю, что этого не заслуживаю, но я не могу не чувствовать себя облегчённой после того, как вы все меня простили."
        m "И я обещаю, что я не сделаю ничего из этого никому из вас снова."
        show monika 1w at t44 zorder 4
        mc "Ну... Не то, чтобы у тебя вообще была такая возможность."
        mc "Теперь я единственный со сверхспособностями."
        mc "И теперь, когда мы все узнали, что же на самом деле произошло, я думаю, мы заслужили небольшой отдых."
        mc "Не всё может быть откачено до исходного состояния."
        show sayori 1k at f41 zorder 4
        s "Этого я и боялась..."
        s 1h "Но я очень надеюсь, что мы сможем привести клуб обратно в порядок."
        show sayori 1g at t41 zorder 3
        mc "Мы смогли вернуть обратно в порядок целый мир!"
        mc "Так почему мы не сможем привести в порядок какой-то клуб?"
        show yuri 2zi at f42 zorder 4
        y "[player] прав, мы сможем сделать что-угодно, если хорошо постараемся."
        show yuri 2s at t42 zorder 2
        show sayori 1d at t41 zorder 3
        show natsuki 5s at f43 zorder 4
        n "..."
        n 5h "Я до сих думаю, что Моника заслуживает какого-то наказания."
        show natsuki 5i at t43 zorder 1
        show yuri 2n at f42 zorder 4
        show sayori 1g at t41 zorder 3
        y "Нацуки!"
        show yuri at t42 zorder 2
        show monika 1ze at f44 zorder 4
        m "Нет, она права."
        m 1x "У вас есть полное право наказать меня за всё, что я сделала."
        show yuri 1zg at t42 zorder 2
        m "Я всё приму..."
        show monika 1w at t44 zorder 3
        show natsuki 5r at f43 zorder 4
        n "..."
        n 5q "Теперь ты заставляешь меня сожалеть об этой идее..."
        n 5y "Но у меня есть идея получше!"
        n 1h "Ты никогда не притронешься к моей манге, усекла?"
        show sayori 1b at t41 zorder 3
        show yuri 1e at t42 zorder 2
        show natsuki 1g at t43 zorder 1
        show monika 1d at f44 zorder 4
        m "И это в-всё?"
        m 1y "Да, я обещаю, что не притронусь."
        show monika 1e at t44 zorder 3
        show natsuki 1z at t43 zorder 1
        show sayori 2l at f41 zorder 4
        s "Ну что же, это было намного проще, чем я могла себе представить."
        show sayori at t41 zorder 4
        mc "Согласен."
        show natsuki 1a at t43 zorder 1
        show yuri 1a at t42 zorder 2
        mc "И теперь, когда всё уже решено, мы начнём работать над всем этим."
        show sayori 1d at t41 zorder 4
        mc "Мы должны дать этому время и идеи, поскольку, кажется, это событие поразило нас всех."
        mc "Но тем не менее, я думаю, мы уже можем и расходиться, время действительно пролетело быстро."
        show sayori 2zc at f41 zorder 4
        s "Увидимся в клубе завтра!"
        show sayori 2d at t41 zorder 4
        show natsuki 5z at t43 zorder 1
        show yuri 2d at t42 zorder 2
        "Мы все машем друг другу, и я с [persistent.sayoriname] идём домой вместе."
        scene bg black with dissolve_scene_full
        stop music fadeout 4.0
        pause(5.0)
        "Следующие несколько дней в клубе были необычайно тихими."
        "Они были гораздо менее активными, Моника не давала никаких домашних заданий по стихам, да и вообще хоть по чему-либо."
        "Но в итоге мы начали прорабатвать это всё вместе..."
        "До тех пор, пока мы и не забыли о том, что в тот день произошло, и жили почти как прежде."
        "Шрамы вроде этого не заживают никогда, но по крайней мере, мы все есть друг у друга."
        scene bg house2 with dissolve_scene_full
        "Я звоню в дверной звонок Монике."
        mc "..."
        show monika 1be at t11 zorder 4
        play music Eternity2
        mc "Привет, Моника."
        mc "Давно не виделись, ты как себя чувствуешь, лучше?"
        show monika 1by at f11 zorder 4
        m "Я всё ещё пытаюсь, и я думаю, я чувствую себя чуточку лучше."
        m 1bg "Но... я до сих пор люблю тебя."
        show monika 1bf at t11 zorder 4
        mc "Это нормально, я и не ожидал, что ты вот так внезапно перестанешь меня любить в ближайшем будущем."
        mc "Может, ты и вовсе никогда не перестанешь меня любить, но помни, что с этим тоже живут."
        mc "Я живу с целой кучей тёмных и неприятных воспоминаний из прошлого, и нормально."
        mc "Уверен, ты сможешь сделать то же самое, я в тебя верю."
        show monika 1by at f11 zorder 4
        m "Спасибо."
        m 1bg "Я не хочу, чтобы это хоть когда-нибудь произошло ещё раз."
        m "Я буду жить с этим бременем вечно, зная, что я хотела навредить тебе и моим друзьям, даже когда ты так сильно меня поддерживал."
        show monika 1bf at t11 zorder 4
        mc "Плохие выборы неизбежны, но тебе не нужно зацикливаться на этом."
        mc "Ты не сможешь изменить прошлое, но ты всегда сможешь изменить будущее."
        show monika 1bg at f11 zorder 4
        m "Ты прав, но я всё ещё не могу забыть."
        m 1by "Но я постараюсь сделать это, ради тебя."
        show monika 1be at t11 zorder 4
        mc "Важнее то, что ты постараешься сделать это ради себя, Моника."
        mc "Но я вижу, что тебе это помогает, поэтому я не против."
        mc "Ладно, ты мне сказала, что хочешь поговорить с Игроком."
        show monika 2bd at f11 zorder 4
        m "Да, очень хочу."
        m 2bg "Но я не хочу удерживать тебя ради этого."
        show monika 2bf at t11 zorder 4
        mc "Эх, Моника, ты забываешь, на что я способен."
        show screen tear(25, 0.05, 0.05, -20, 80)
        play sound "sfx/glitch2.ogg"
        window hide
        pause(0.6)
        hide screen tear
        show monika 1bd at t22 zorder 3
        show baryon 1bp at t21 zorder 4
        pause(1.0)
        show baryon 1bd at f21 zorder 4
        mc "Вот, теперь ты должна его увидеть."
        show baryon 2bg at f21 zorder 4
        mc "Думаю, я оставлю вас двоих, а сам вернусь к [persistent.sayoriname]."
        show baryon 1bg at f21 zorder 4
        mc "Наслаждайтесь времяпровождением, голубки!"
        show baryon at thide zorder 4
        hide baryon
        show monika 1be at t22 zorder 4
        pause(2.0)
        show monika 1by at f11 zorder 4
        m "Привет..."
        m "Наконец-то мне перепала возможность поговорить с тобой."
        m 1bg "Даже если я этого совсем не заслуживаю, после всего, что я сделала."
        m "И мне очень жаль за всё то, что тебе пришлось увидеть."
        m "Но прежде чем мы начнём, я хочу у тебя кое-что спросить."
        menu:
            m "Ты прощаешь меня?"
            "Да":
                $ value = 18
            "Нет":
                $ value = 19
        if value == 18:
            m 1bd "..."
            m 1by "П-правда что ли?"
            m "Спасибо тебе, это очень много для меня значит..."
            m 1bg "Я хочу, чтобы у меня был шанс искупить всю свою прошлую вину."
            m "И я знаю, что я прошу слишком многого, особенно после того, как я хотела навредить всем моим друзьям."
            m 1bx "Я больше никогда не сделаю это снова, я обещаю."
            jump phase9
        if value == 19:
            m 1bz "Я этого и ожидала..."
            m 1bx "Но я понимаю, я делала ужасные вещи, и одным простым прощением всё не исправить."
            m 1bz "..."
            m 1bx "Пожалуйста, знай, что я стараюсь, чтобы искупить свою вину."
            m "Так что даже если ты не простишь меня, я была бы очень благодарна за то, что ты поверил, что я смогу измениться."
            jump phase9
label phase9:
    m 1bze "И, может быть, однажды, мы сможем выбраться из моего мира в твой..."
    m "Я очень хочу проводить время с моими друзьями."
    m "И с моим возлюбленным, даже если он сам не любит меня."
    m 2by "Было бы просто замечательно, не так ли?"
    m "Все виды, которые мы сможем увидеть, все моменты, которые мы сможем испытать."
    m 1by "Но я счастлива и с тем, что у меня есть."
    m "[player] простил меня, да и остальные тоже."
    m 1bze "Они лучшие друзья, о которых я когда-либо могла желать."
    m 1bx "И мне стоило начать ценить их раньше..."
    m 1by "Но мы прорабатываем всякое разное в последнее время, и мы уже почти пришли к исходному состоянию."
    m 1bd "Ох..."
    m 2bl "Что-то я заговорилась, не так ли?"
    m 2bb "Так что я возвращаю свою перспективу обратно к тому, что видит [player]."
    m 1by "Надеюсь, мы сможем поговорить как-нибудь ещё раз."
    m "Пока!"
    scene bg black with dissolve_scene_full
    stop music fadeout 4.0
    pause(2.0)
    scene bg house with dissolve_scene_full
    pause(1.0)
    show sayori 1ba at t11 zorder 4
    mc "Привет, [persistent.sayoriname]."
    play music t10
    mc "Я тут думал над кое-чем в последнее время..."
    show sayori 1bb at t11 zorder 4
    mc "Ни у кого из нас нет больше никаких скелетов в шкафу, и всё такое."
    mc "У тебя, случаем, остались ли ещё вопросы или сомнения по поводу всего, что произошло?"
    show sayori 2bc at f11 zorder 4
    s "Да, есть что-то, что я хотела спросить."
    s 1bh "Моника до сих пор ненавидит меня?"
    show sayori 1bg at t11 zorder 4
    mc "Я не уверен, я же не знаю, что у неё в голове."
    mc "Но она извинилась перед тобой, и я не думаю, что у неё остались какие-то плохие чувства к тебе."
    mc "Она пыталась навредить тебе несколько раз, даже открыто противостояла тебе ранее."
    mc "Но на сегодняшний день, она была довольно мила с тобой, верно?"
    show sayori 2bzc at f11 zorder 4
    s "Да, мы разговариваем чуть больше сейчас."
    s 2bh "Но я не могу сказать, что всё из того, что было между нами, такое же, как и сейчас."
    s "И это не столько обо мне самой, я больше беспокоюсь за неё."
    s 1bh "Она же до сих пор любит тебя, не так ли?"
    show sayori 1bg at t11 zorder 4
    mc "Конечно, и у меня такое ощущение, что она никогда и не перестанет."
    mc "Я любил её как друга, но увы... для неё это гораздо серьёзнее, чем для меня."
    mc "И она продолжает вредить самой себе, даже если это уже не настолько плохо, как тогда, когда она противилась тебе."
    mc "Я не думаю, что она скажет что-то подобное снова..."
    mc "Но не переживай, я часто её навещаю, как она вообще, и она выглядит гораздо спокойнее по этому поводу."
    show sayori 2bzc at f11 zorder 4
    s "Вот так облегчение."
    s 1bh "Она пыталась навредить мне и всем остальным, но она всё ещё мой друг."
    s "И я знаю, что она находится под давлением, сама бы она так не сделала."
    s 1bzc "Она всегда была такой заботливой и понимающей."
    s 2bzc "Поэтому я стараюсь ей помочь изо всех сил."
    show sayori 2bd at t11 zorder 4
    mc "За это я тебя и люблю."
    mc "Несмотря на то, что у тебя есть сотня причин, чтобы этого не делать, ты всё равно это сделаешь."
    mc "Мы оба хотим сделать всё правильно, и однажды у нас обязательно получится."
    show sayori 1bzc at f11 zorder 4
    s "Ты прав."
    s 1bzd "[player]{w=0.25}.{w=0.25}.{w=0.25}. это уже было так давно, когда я ещё думала, что у меня нет причин жить."
    s 2bzd "Но ты дал мне надежду, ты дал мне шанс продолжать."
    s "Ты стал моим..."
    s 1bzd "...моим Спасением."
    s 4bzd "Я не могу передать словами, насколько сильно я хочу отблагодарить тебя за всё."
    show sayori 4bt at t11 zorder 4
    mc "Тебе правда не стоит, [persistent.sayoriname]..."
    mc "Я знаю, что это чистая правда, и я очень счастлив, что ты сделала правильный выбор."
    mc "Но второй шанс тебе дал не только я."
    mc "Не было бы вообще никого, если бы ты не решила остаться со мной и дать самой себе второй шанс."
    show sayori 1bv at f11 zorder 4
    s "Но, [player], разве мы действительно в безопасности?"
    show sayori at t11 zorder 4
    mc "Вне зависимости от того, кто или что с нами произойдёт, тебе не нужно бояться."
    mc "Я не позволю никому навредить тебе или моим друзьям."
    show sayori 1bt at t11 zorder 4
    mc "Мы всегда будем вместе, и никто нас не разлучит."
    scene bg black with dissolve_scene_full
    stop music fadeout 5.5
    pause(2.5)
    "Обещаю."
    scene bg black with dissolve_scene_full
    pause(2.0)
    $ renpy.movie_cutscene("bg/GoodEnding.webm")
    jump phase10
    
label phase10:
    pause(0.01)
