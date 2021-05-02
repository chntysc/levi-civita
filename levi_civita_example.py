class ContohLeviCivita(Scene):
    def construct(self):
        
        judul = TextMobject("Contoh Soal levi-Civita").scale(2).set_color_by_gradient(RED_C, YELLOW_C)
        desk = TextMobject("Buktikan").scale(1).set_color(RED_C)
        soal = TexMobject("\sum_{}^{n} \in_{ijk} \in_{ijk} = 6 , n= 1,2,3").scale(1).set_color(RED_C)
        textjawab = TextMobject("Jawab : ").scale(1).set_color(RED_C)
        desk.to_corner(UL)
        soal.next_to(desk, DOWN).align_to(desk, LEFT)
        textjawab.next_to(soal, DOWN).align_to(desk, LEFT)

        self.play(ShowCreation(judul))
        self.wait(2)
        self.play(ReplacementTransform(judul, desk),
                  ShowCreation(soal),
                  ShowCreation(textjawab),
                  )
        jwb = TexMobject("\sum_{k=1}^{3}\sum_{j=1}^{3}\sum_{i=1}^{3} \in_{ijk} \in_{ijk}",  # 0
                          "=",  # 1
                          "\sum_{k=1}^{3}\sum_{j=1}^{3} [ \in_{1jk} \in_{1jk} + \in_{2jk} \in_{2jk} + \in_{3jk} \in_{3jk}", #2
                          "\sum_{k=1}^{3}", #3
                          "\in_{11k} \in_{11k} ",#4
                          "+ \in_{21k} \in_{21k} + \in_{31k} \in_{31k} + ",  #5
                          "\in_{12k} \in_{12k} + " , #6
                          "\in_{22k} \in_{22k}  ", #7
                          "+\in_{32k} \in_{32k}+",  #8
                          "\in_{13k} \in_{13k} + \in_{23k} \in_{23k} + ", #9
                          "\in_{33k} \in_{33k}"  #10
                          ).scale(0.8).set_color(BLUE_B)
        jwb[0].next_to(textjawab,DOWN).align_to(textjawab,LEFT)
        jwb[1].next_to(jwb[0],RIGHT)
        jwb[2].next_to(jwb[1],RIGHT)
        jwb[3].next_to(jwb[1],RIGHT)
        self.play(Write(jwb[0]),Write(jwb[1]),Write(jwb[2]))
        self.play(ReplacementTransform(jwb[2],jwb[3]))

        jwb[4].next_to(jwb[3], RIGHT)
        jwb[5].next_to(jwb[4], RIGHT)
        jwb[6].next_to(jwb[4], DOWN).align_to(jwb[4],LEFT)
        jwb[7].next_to(jwb[6], RIGHT)
        jwb[8].next_to(jwb[7], RIGHT)
        jwb[9].next_to(jwb[6], DOWN).align_to(jwb[4], LEFT)
        jwb[10].next_to(jwb[9], RIGHT)


        self.play(Write(VGroup(jwb[4],jwb[5],jwb[6],jwb[7],jwb[8],jwb[9],jwb[10])))


        diket = TexMobject("Ingat !! ",
                            "i,j,k [repeat] \\rightarrow \in_{ijk}=0",
                            "i,j,k [anticyclic] \\rightarrow \in_{ijk}=-1",
                            "i,j,k [cyclic] \\rightarrow \in_{ijk}=1"
                            ).scale(0.7).set_color(RED_C)
        diket[0].move_to(UP*3)
        diket[1].next_to(diket[0],DOWN).align_to(diket[0],LEFT)
        diket[2].next_to(diket[1],DOWN).align_to(diket[0],LEFT)
        diket[3].next_to(diket[2],DOWN).align_to(diket[0],LEFT)

        self.play(ShowCreation(diket))
        frameboxingat= SurroundingRectangle(diket, buff=.1,color=MAROON_B)
        self.play(ShowCreation(frameboxingat))
        self.play(WiggleOutThenIn(diket[1]))

        framebox1 = SurroundingRectangle(jwb[4], buff=.1,color=RED_C)
        framebox2 = SurroundingRectangle(jwb[7], buff=.1,color=RED_C)
        framebox3 = SurroundingRectangle(jwb[10], buff=.1,color=RED_C)

        self.play(ShowCreation(VGroup(framebox1,framebox2,framebox3)))
        self.wait(2)


        diket1=TextMobject(" i=j , so the value would be 0 ").scale(0.7).set_color(RED_C)

        diket1.next_to(jwb[9],DOWN)
        self.play(Write(diket1))
        self.wait(2)
        pengganti = TextMobject("0",
                                "0",
                                "0",
                                ).scale(0.8).set_color(BLUE_B)

        pengganti[0].next_to(jwb[3], RIGHT)
        pengganti[1].next_to(jwb[6], RIGHT)
        pengganti[2].next_to(jwb[9], RIGHT)

        self.play(Transform(jwb[4],pengganti[0]),
                  Transform(jwb[7],pengganti[1]),
                  Transform(jwb[10],pengganti[2])
        )
        self.wait()

        pers=TexMobject("\in_{211}\in_{211}+\in_{212} \in_{212}+", #0
                        "\in_{213} \in_{213}+", #1
                        "\in_{311} \in_{311}+",#2
                        "\in_{312} \in_{312}+",#3
                        "\in_{313} \in_{313}+",#4
                        "\in_{121} \in_{121}+\in_{122} \in_{122} + ", #5
                        "\in_{123} \in_{123}+", #6
                        "\in_{321} \in_{321}+", #7
                        "\in_{322} \in_{322}+\in_{323} \in_{323}+", #8
                        "\in_{131} \in_{131}+", #9
                        "\in_{132} \in_{132}+ ", #10
                        "\in_{133} \in_{133}+", #11
                        "\in_{231} \in_{231}+", #12
                        "\in_{232} \in_{232}+\in_{233} \in_{233}" #13
        ).scale(0.8).set_color(BLUE_B)
        pers[0].next_to(jwb[1],RIGHT)
        pers[1].next_to(pers[0],RIGHT)
        pers[2].next_to(pers[0],DOWN).align_to(pers[0],LEFT)
        pers[3].next_to(pers[2], RIGHT)
        pers[4].next_to(pers[3], RIGHT)
        pers[5].next_to(pers[2], DOWN).align_to(pers[0], LEFT)
        pers[6].next_to(pers[5], RIGHT)
        pers[7].next_to(pers[5], DOWN).align_to(pers[0], LEFT)
        pers[8].next_to(pers[7], RIGHT)
        pers[9].next_to(pers[7], DOWN).align_to(pers[0], LEFT)
        pers[10].next_to(pers[9], RIGHT)
        pers[11].next_to(pers[10], RIGHT)
        pers[12].next_to(pers[11], DOWN).align_to(pers[0], LEFT)
        pers[13].next_to(pers[12], RIGHT)

        self.play(ReplacementTransform(jwb[5],pers[0:5]),
                  ReplacementTransform(jwb[6],pers[5:7]),
                  ReplacementTransform(jwb[8],pers[7:9]),
                  ReplacementTransform(jwb[9],pers[9:13]),
                  Write(pers[13]),
                  FadeOut(diket1),
                  FadeOut(VGroup(framebox1,framebox2,framebox3,jwb[4],jwb[7],jwb[10],jwb[3])),
                  )


        zero = TextMobject("0   +   0    +", #0
                           "0  + ", #1
                           "0  +", #2
                           "0   +   0  + ", #3
                           "0   +   0  +", #4
                           "0    +", #5
                           "0   +", #6
                           "0   +   0" #7
                           ).scale(0.8).set_color(BLUE_B)

        zero[0].move_to(pers[0])
        zero[1].move_to(pers[2])
        zero[2].move_to(pers[4])
        zero[3].move_to(pers[5])
        zero[4].move_to(pers[8])
        zero[5].move_to(pers[9])
        zero[6].move_to(pers[11])
        zero[7].move_to(pers[13])

        self.play(WiggleOutThenIn(diket[1]))
        self.wait()
        self.play(WiggleOutThenIn(VGroup(pers[2],pers[0],pers[4],pers[5],pers[8],pers[9],pers[11],pers[13])))
        self.wait(2)
        self.play(ReplacementTransform(VGroup(pers[2],pers[0],pers[4],pers[5],pers[8],pers[9],pers[11],pers[13]),zero))



        satu = TextMobject ("(-1.-1) +",
                            "(-1.-1) +",
                            "1 +",
                            "(-1.-1) +",
                            "1 +",
                            "1 +",
                            ).scale(0.8).set_color(BLUE_B)
        satu[0].move_to(pers[1])
        satu[1].move_to(pers[3])
        satu[2].move_to(pers[6])
        satu[3].move_to(pers[7])
        satu[4].move_to(pers[10])
        satu[5].move_to(pers[12])

        self.play(WiggleOutThenIn(diket[2]),run_time=1.5)
        self.play(WiggleOutThenIn(VGroup(pers[1], pers[3], pers[7])),run_time=2)
        self.wait()
        self.play(ReplacementTransform(VGroup(pers[1],pers[3],pers[7]), VGroup(satu[0],satu[1],satu[3])))

        self.play(WiggleOutThenIn(diket[3]),run_time=1.5)
        self.play(WiggleOutThenIn(VGroup(pers[6], pers[10], pers[12])),run_time=2)
        self.play(ReplacementTransform(VGroup(pers[6], pers[10], pers[12]), VGroup(satu[2], satu[4], satu[5])))

        hasil = TexMobject("6").scale(0.8).set_color(BLUE_B)
        hasil.next_to(jwb[1],RIGHT)

        self.play(ReplacementTransform(VGroup(satu,zero),hasil))
        self.play(FadeOut(VGroup(diket,frameboxingat)))

        framebox = SurroundingRectangle(soal, buff=.1)
        self.play(ShowCreation(framebox))
        terbukti = TextMobject("Terbukti !! ").scale(1).set_color_by_gradient(RED_C, YELLOW_C)
        terbukti.next_to(soal, RIGHT * 1)
        self.play(ReplacementTransform(desk, terbukti))
        self.wait()

        jawaban = VGroup(framebox, soal, terbukti)
        self.play(FadeOut(VGroup(hasil, textjawab,jwb[0],jwb[1])))
        self.play(
            jawaban.shift, RIGHT * 3 + DOWN * 2,
            run_time=2
        )

        self.wait()
