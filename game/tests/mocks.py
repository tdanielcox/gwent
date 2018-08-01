import copy


def full_game():
    return copy.deepcopy({
        "status": ["round_0_start", "player_1_start"],
        "current_player": 0,
        "loser": None,
        "id": "5104b41c-a61c-4532-8767-21f77cb68416",
        "players": [
            {
                "lost": False,
                "losses": [False, False],
                "points": 0,
                "passed": [False, False, False],
                "cards": [
                    [
                        ["Biting Frost", 0, 0, 6, 0, "neutral/biting-frost.png", "9098b28e-82da-40f7-93c9-1b55c156ee51", 0],
                        ["Blue Stripes Commando", 0, 4, 1, 2, "northern-realms/blue-stripes-commando.png", "c4acb180-3553-45fc-b649-905dd9a6f75e", 4],
                        ["Blue Stripes Commando", 0, 4, 1, 2, "northern-realms/blue-stripes-commando.png", "64948108-1b28-41e2-9810-193b92418322", 4],
                        ["Prince Stennis", 0, 5, 2, 0, "northern-realms/prince-stennis.png", "15e3ff97-8ba3-4455-89dd-bd889e25bbb8", 5],
                    ],
                    [

                    ],
                    [
                        ["Catapult", 2, 8, 1, 4, "northern-realms/catapult.png", "5f6ed576-3791-4d54-82b4-dc06e302955d", 8],
                        ["Catapult", 2, 8, 1, 4, "northern-realms/catapult.png", "f8402a3b-6f35-4600-852c-cb6af929bc19", 8],
                        ["Kaedweni Siege Expert", 2, 1, 4, 0, "northern-realms/kaedweni-siege-expert.png", "e4e229b0-16d7-41f2-a6b1-9b4746561e55", 1],
                        ["Kaedweni Siege Expert", 2, 1, 4, 0, "northern-realms/kaedweni-siege-expert.png", "7894d713-bc7d-403e-aab5-868e5b12c685", 1],
                        ["Thaler", 2, 1, 2, 0, "northern-realms/thaler.png", "94696a86-409c-4c0d-b4b1-bdafd1b7ade6", 1]
                    ],
                    [
                        ["Clear Weather", 3, 0, 6, 0, "neutral/clear-weather.png", "2dbee300-6ee9-49a9-b0e0-8207c9e14c76", 0]
                    ]
                ],
                "unused_cards": [
                    ["Siegfried of Denesle", 0, 5, 0, 0, "northern-realms/siegfried-of-denesle.png", "2b583516-4ca9-479b-8cb2-36113319a1af", 5],
                    ["Ves", 0, 5, 0, 0, "northern-realms/ves.png", "bef8ab9c-46a7-4497-8726-b0f8787cd255", 5],
                    ["Blue Stripes Commando", 0, 4, 1, 2, "northern-realms/blue-stripes-commando.png", "ba76e8a3-bc05-4ed2-afaa-58e823248da9", 4],
                    ["Sigismund Dijkstra", 0, 4, 2, 0, "northern-realms/sigismund-dijkstra.png", "bd15a99c-7cc9-47cd-a7cb-8e33e412fbf2", 4],
                    ["Esterad Thyssen", 0, 10, 3, 0, "northern-realms/esterad-thyssen.png", "64c16d79-76d2-49b9-ae9d-bf42e78615a6", 10],
                    ["John Natalis", 0, 10, 3, 0, "northern-realms/john-natalis.png", "e6d20008-686e-49a0-874c-3e83f15a9448", 10],
                    ["Vernon Roche", 0, 10, 3, 0, "northern-realms/vernon-roche.png", "b8b59a8d-41d1-4996-bc48-a49e962f4b76", 10],
                    ["Sheldon Skaggs", 1, 4, 0, 0, "northern-realms/sheldon-skaggs.png", "01d8c5a5-5e3f-4383-912e-6db7eb9e215f", 4],
                    ["Sabrina Glevissig", 1, 4, 0, 0, "northern-realms/sabrina-glevissig.png", "48cc3ca6-4e7f-4dcb-a523-353ad8c1d069", 4],
                    ["Sile de Tansarville", 1, 5, 0, 0, "northern-realms/sile-de-tansarville.png", "29d8fcf5-e810-457e-bc6c-c214391d252b", 5],
                    ["Crinfrid Reavers Dragon Hunter", 1, 5, 1, 3, "northern-realms/crinfrid-reavers-dragon-hunter.png", "30885249-7803-40fe-91ee-488534f6d8ef", 5],
                    ["Crinfrid Reavers Dragon Hunter", 1, 5, 1, 3, "northern-realms/crinfrid-reavers-dragon-hunter.png", "c92378de-a56c-4d06-a1c7-bdc85c21c5b6", 5],
                    ["Crinfrid Reavers Dragon Hunter", 1, 5, 1, 3, "northern-realms/crinfrid-reavers-dragon-hunter.png", "2130befa-157e-4065-8b71-d88caeb5663c", 5],
                    ["Keira Metz", 1, 5, 0, 0, "northern-realms/keira-metz.png", "0c95ef22-604a-4765-a9e6-4c6786497fc9", 5],
                    ["Dethmold", 1, 6, 0, 0, "northern-realms/dethmold.png", "1d0e79bb-74ff-4427-926f-81c775b67e3b", 6],
                    ["Philippa Eilhart", 1, 10, 3, 0, "northern-realms/philippa-eilhart.png", "5b97802a-f387-45fe-9b39-87846a60e7df", 10],
                    ["Trebuchet", 2, 6, 0, 0, "northern-realms/trebuchet.png", "2baef9cb-5640-484c-b4cf-e05c060661bc", 6],
                    ["Siege Tower", 2, 6, 0, 0, "northern-realms/siege-tower.png", "33230aea-f8d1-4c79-bc83-429b8407c7fb", 6],
                    ["Trebuchet", 2, 6, 0, 0, "northern-realms/trebuchet.png", "93bc9ebb-f2f3-42b4-8109-c97d4f6368b1", 6],
                    ["Ballista", 2, 6, 0, 0, "northern-realms/ballista.png", "dce6efc6-b227-4a05-b54d-a05e0cbefb88", 6],
                    ["Ballista", 2, 6, 0, 0, "northern-realms/ballista.png", "5413eae9-6a5a-4e4f-a24a-de19c527ee8e", 6],
                    ["Impenetrable Fog", 1, 0, 6, 0, "neutral/impenetrable-fog.png", "babc4339-a0a9-4a62-ba41-66569c9327b7", 0],
                    ["Torrential Rain", 2, 0, 6, 0, "neutral/torrential-rain.png", "c8101a73-2e9b-42b1-8104-64f882e5de84", 0],
                    ["Scorch", 3, 0, 7, 0, "neutral/scorch.png", "adb65832-dd82-4b94-b3e3-7c55781e375e", 0],
                    ["Scorch", 3, 0, 7, 0, "neutral/scorch.png", "b52f8594-9d99-49b5-bf36-7c9328c6d7fe", 0]
                ]
            },
            {
                "lost": False,
                "losses": [False, False],
                "points": 0,
                "passed": [False, False, False],
                "cards": [
                    [
                        ["Biting Frost", 0, 0, 6, 0, "neutral/biting-frost.png", "00673012-3f0b-4dd3-8d95-aabaaf4765ac", 0],
                        ["Blue Stripes Commando", 0, 4, 1, 2, "northern-realms/blue-stripes-commando.png", "90a49883-eb8d-4b6c-8cf7-27bf7dfdb2bc", 4],
                        ["Ves", 0, 5, 0, 0, "northern-realms/ves.png", "6e782f42-4aaa-497a-8e01-204216714c7e", 5],
                    ],
                    [
                        ["Crinfrid Reavers Dragon Hunter", 1, 5, 1, 3, "northern-realms/crinfrid-reavers-dragon-hunter.png", "65311fe9-c124-4deb-b75c-fc5361135ee6", 5],
                        ["Crinfrid Reavers Dragon Hunter", 1, 5, 1, 3, "northern-realms/crinfrid-reavers-dragon-hunter.png", "b89597a8-0fc4-45e5-9498-e5aa8fdd9c67", 5],
                        ["Keira Metz", 1, 5, 0, 0, "northern-realms/keira-metz.png", "727481c1-cc45-480f-b171-3683bcfb7335", 5],
                    ],
                    [
                        ["Kaedweni Siege Expert", 2, 1, 4, 0, "northern-realms/kaedweni-siege-expert.png", "25f39df2-037e-496a-b4be-82dbd9dedbe3", 1],
                        ["Siege Tower", 2, 6, 0, 0, "northern-realms/siege-tower.png", "756b252f-dda6-4aba-b599-3943e57c2bd4", 6],
                        ["Torrential Rain", 2, 0, 6, 0, "neutral/torrential-rain.png", "b6cfe466-e543-412c-9199-9060baa21e01", 0]
                    ],
                    [
                        ["Scorch", 3, 0, 7, 0, "neutral/scorch.png", "d79c03b1-2ae2-4131-8d50-220129b9c5b2", 0]
                    ]
                ],
                "unused_cards": [
                    ["Blue Stripes Commando", 0, 4, 1, 2, "northern-realms/blue-stripes-commando.png", "c6131212-5848-471c-95c2-63ebe9928b49", 4],
                    ["Blue Stripes Commando", 0, 4, 1, 2, "northern-realms/blue-stripes-commando.png", "f1c41268-5274-4a02-89d6-1b231ff8026c", 4],
                    ["Sigismund Dijkstra", 0, 4, 2, 0, "northern-realms/sigismund-dijkstra.png", "c977d483-b656-4532-99b9-b03d646377a5", 4],
                    ["Siegfried of Denesle", 0, 5, 0, 0, "northern-realms/siegfried-of-denesle.png", "78e3ca6d-b4bf-426b-9d9d-bb8de12723bb", 5],
                    ["Prince Stennis", 0, 5, 2, 0, "northern-realms/prince-stennis.png", "d5cd014a-4563-4ab1-b3b9-8b3e49365c61", 5],
                    ["Esterad Thyssen", 0, 10, 3, 0, "northern-realms/esterad-thyssen.png", "bce963c0-84ba-4175-a701-4759a1f7c0e6", 10],
                    ["John Natalis", 0, 10, 3, 0, "northern-realms/john-natalis.png", "23d71c7e-e19e-4516-af8f-51b1ce6357a9", 10],
                    ["Vernon Roche", 0, 10, 3, 0, "northern-realms/vernon-roche.png", "c9333630-54b9-4e9f-b84f-3bc49bada30d", 10],
                    ["Sile de Tansarville", 1, 5, 0, 0, "northern-realms/sile-de-tansarville.png", "66fb4d4e-0f7c-4f35-b5b2-4388eccb0c1c", 5],
                    ["Sabrina Glevissig", 1, 4, 0, 0, "northern-realms/sabrina-glevissig.png", "1fe8bb94-48b0-42f5-a29e-eb7aa7040202", 4],
                    ["Sheldon Skaggs", 1, 4, 0, 0, "northern-realms/sheldon-skaggs.png", "334e9bcc-47a3-46e7-86ef-f435a2185810", 4],
                    ["Crinfrid Reavers Dragon Hunter", 1, 5, 1, 3, "northern-realms/crinfrid-reavers-dragon-hunter.png", "b118d15f-c026-4ab5-bc04-b6f622385ff8", 5],
                    ["Dethmold", 1, 6, 0, 0, "northern-realms/dethmold.png", "a48b5f57-7e59-4bbc-84ac-514932421775", 6],
                    ["Philippa Eilhart", 1, 10, 3, 0, "northern-realms/philippa-eilhart.png", "cdcbdcb5-129b-436d-8408-2eec7727a937", 10],
                    ["Ballista", 2, 6, 0, 0, "northern-realms/ballista.png", "dba8a9a3-31c5-4e77-bb8e-2f7afcab678e", 6],
                    ["Kaedweni Siege Expert", 2, 1, 4, 0, "northern-realms/kaedweni-siege-expert.png", "16902580-efaf-4733-83e7-27a55b80c731", 1],
                    ["Thaler", 2, 1, 2, 0, "northern-realms/thaler.png", "b6b6adaf-27c8-498e-b18e-0b82d2a07d69", 1],
                    ["Trebuchet", 2, 6, 0, 0, "northern-realms/trebuchet.png", "52e4ea36-9ecf-46d4-bd2e-21d29c5c4cac", 6],
                    ["Trebuchet", 2, 6, 0, 0, "northern-realms/trebuchet.png", "7ffa74fc-d66f-4d93-b919-0f4a14e2b4d9", 6],
                    ["Ballista", 2, 6, 0, 0, "northern-realms/ballista.png", "79164c10-a7ac-4793-9f95-d4e56d299e96", 6],
                    ["Catapult", 2, 8, 1, 4, "northern-realms/catapult.png", "a232d78d-a398-4cab-85b6-238262d3b313", 8],
                    ["Catapult", 2, 8, 1, 4, "northern-realms/catapult.png", "06fae3f4-fcab-46b1-999d-18e9ac2b5a96", 8],
                    ["Impenetrable Fog", 1, 0, 6, 0, "neutral/impenetrable-fog.png", "194fb7e7-f551-48e6-9876-624e8de249b6", 0],
                    ["Clear Weather", 3, 0, 6, 0, "neutral/clear-weather.png", "a99bb4f5-ae53-4b6e-9427-b3a2ceca8b6b", 0],
                    ["Scorch", 3, 0, 7, 0, "neutral/scorch.png", "de66b86d-ccb2-49e1-accd-013b28de9211", 0]
                ]
            }
        ],
        "rounds": [
            {
                "cards": [
                    [
                        [], [], []
                    ],
                    [
                        [], [], []
                    ]
                ],
                "winner": None,
                "scores": {
                    "cards": [[[], [], []], [[], [], []]],
                    "rows": [[0, 0, 0], [0, 0, 0]],
                    "totals": [0, 0]
                }
            },
            {
                "cards": [[[], [], []], [[], [], []]],
                "winner": None,
                "scores": {
                    "cards": [[[], [], []], [[], [], []]],
                    "rows": [[0, 0, 0], [0, 0, 0]],
                    "totals": [0, 0]
                }
            },
            {
                "cards": [[[], [], []], [[], [], []]],
                "winner": None,
                "scores": {
                    "cards": [[[], [], []], [[], [], []]],
                    "rows": [[0, 0, 0], [0, 0, 0]],
                    "totals": [0, 0]
                }
            }
        ],
        "round": 0
    })
