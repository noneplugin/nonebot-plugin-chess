## nonebot-plugin-chess

适用于 [Nonebot2](https://github.com/nonebot/nonebot2) 的国际象棋插件。


### 安装

- 使用 nb-cli

```
nb plugin install nonebot_plugin_chess
```

- 使用 pip

```
pip install nonebot_plugin_chess
```


人机功能 需要使用遵循 [UCI协议](https://www.xqbase.com/protocol/uci.htm) 的引擎

需要在 `.env` 文件中添加 引擎的可执行文件的路径

```
chess_engine_path=/path/to/your/engine
```

推荐的引擎：

 - [Stockfish](https://stockfishchess.org/)


### 使用

**以下命令需要加[命令前缀](https://v2.nonebot.dev/docs/api/config#Config-command_start) (默认为`/`)，可自行设置为空**

@我 + “国际象棋人机”或“国际象棋对战”开始一局游戏；

可使用“lv1~8”指定AI等级，如“国际象棋人机lv5”，默认为“lv4”；

发送 起始坐标格式，如“e2e4”下棋；

在坐标后加棋子字母表示升变，如“e7e8q”表示升变为后；

对应的字母：K：王，Q：后，B：象，N：马，R：车，P：兵

发送“结束下棋”结束当前棋局；

发送“显示棋盘”显示当前棋局；

发送“悔棋”可进行悔棋（人机模式可无限悔棋；对战模式只能撤销自己上一手下的棋）；


或者使用 `chess` 指令：

可用选项：

 - `-e`, `--stop`, `--end`: 停止下棋
 - `-v`, `--show`, `--view`: 显示棋盘
 - `--repent`: 悔棋
 - `--reload`: 重新加载已停止的游戏
 - `--battle`: 对战模式，默认为人机模式
 - `--black`: 执黑，即后手
 - `-l <LEVEL>`, `--level <LEVEL>`: 人机等级，可选 1~8，默认为 4


### 示例

<div align="left">
    <img src="https://s2.loli.net/2022/05/02/1gqSQUfnLuvkpAm.png" width="500" />
</div>


### 特别感谢

- [niklasf/python-chess](https://github.com/niklasf/python-chess) A chess library for Python
- [official-stockfish/Stockfish](https://github.com/official-stockfish/Stockfish) UCI chess engine
