# rutgerklamer/brnfck-chat

⭐ 6 · JavaScript · MIT · 推送 2026-11-03 · [GitHub](https://github.com/rutgerklamer/brnfck-chat) · [官网](https://brnfck.chat) · 个人维护

**用 8 个字符的 brainfuck 程序运行语言模型的聊天项目**

将 SmolLM2-135M、Qwen2.5-0.5B/1.5B、Qwen3.5-0.8B（含视觉版）等小模型编译为仅含 `+ - < > [ ] , .` 八个命令的单文件 brainfuck 程序，输入问题后打印模型生成的回答；其中一个程序以 brainfuck 代码作答。README 给出从 Hugging Face 下载模型权重、用 Node 脚本编译并验证、通过 CLI 或本地网页提问的完整流程；另含 4 个在 brainfuck 内自行训练网络的程序。仅支持小参数量模型，大程序需数十 GB 磁盘与内存。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 个聊天程序：模型权重编译为纯 brainfuck 单文件程序
- Qwen3.5-0.8B 视觉版可读取图片后回答
- Qwen2.5-Coder 版以 brainfuck 程序作答并通过测试用例
- 4 个在 brainfuck 内训练网络的程序及其自打印后代

## 适用场景

- 在网页聊天界面用编译出的 brainfuck 程序回答问题
- 查看程序地图与逐层输出，了解模型内部数值
- 在 brainfuck 内从随机数训练小型网络并观察代际演化

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3:  A chatbot written in eight characters: <code>&gt; &lt; + - [ ] , .</code>
> L4:  Type a question. A program written in brainfuck prints the answer.
> L15: and read or print characters. Here those commands run a language model. Each program is one text

## 星数曲线

```mermaid
xychart-beta
    title "rutgerklamer/brnfck-chat 星数(近 3 点)"
    x-axis ["2026-10-28", "2026-11-08", "2026-11-27"]
    y-axis "stars" 4 --> 7
    line [5, 6, 6]
```

2026-10-28 5 → 2026-11-27 6（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 mid · 依据 README sha `c9a10f9f0cd4` · [字段定义](../../DATASET.md)*
