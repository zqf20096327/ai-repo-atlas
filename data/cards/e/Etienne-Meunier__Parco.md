# Etienne-Meunier/Parco

⭐ 3 · Python · MIT · 推送 2026-11-23 · [GitHub](https://github.com/Etienne-Meunier/Parco) · 个人维护

**让 AI 以读者身份参与 LaTeX 写作的迭代修订工具**

开源（MIT）的 LaTeX 协作写作工具：AI agent 读取文档后以批注、修订、参考文献建议的形式提交提案，作者在本地评审平台中逐条接受、拒绝或讨论，未被接受的修改不写入 .tex 源文件。提供 reference/comment/proofread/generative 四种阅读模式与 %parco、\cite{parco} 两个标记控制 AI 写作位置；每次关闭版本后 AI 上下文清空，下一版仅审阅增量改动。所有 AI 动作经 parco 命令行按模式与阶段校验。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 diff 形式呈现全部提案，作者逐条接受/拒绝/讨论后才写入源文件
- 四种阅读模式金字塔式叠加，%parco 标签限定 AI 写作位置
- 版本关闭即清空 AI 记忆，仅增量审阅上次改动
- AI 动作经 parco 命令行按模式与阶段强制校验

## 适用场景

- 论文写作中让 AI 只做校对与批注而不代写
- 为草稿中的 \cite{parco} 占位符补全真实参考文献
- 反复迭代修改时避免把整篇文档反复发给 AI

## 场景标签

`科研工具` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L5: Parco is a small, free and open-source tool for writing LaTeX documents alongside an AI, iteratively, with track cha
> L17: - **You stay the author.** The AI only writes new text where you explicitly ask for it, with a `%parco` tag. Elsewh
> L21: - **Rules enforced by the program, not by the prompt.** Every action of the AI goes through the `parco` command lin
> L50: Parco works with any AI agent able to run shell commands: Claude Code, ChatGPT / Codex, Gemini CLI, Cursor and othe


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `05507e55973a` · [字段定义](../../DATASET.md)*
