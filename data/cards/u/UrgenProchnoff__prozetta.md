# UrgenProchnoff/prozetta

⭐ 12 · JavaScript · MIT · 推送 2026-11-11 · [GitHub](https://github.com/UrgenProchnoff/prozetta) · 个人维护 · 中文 README

**面向小说翻译者的 LLM 分章流水线，含术语表与自检循环**

用语言模型翻译虚构书籍的程序：全书先抽取术语表与叙事设定（passport），逐段翻译时随段注入相关术语与设定，并由独立模型调用打分（0-10）决定接受、修正或重译，每段最多十次尝试。全书级审校发现不自动应用，由人工逐条接受后进入修正队列。程序本地运行于浏览器界面，支持云或本地模型，导出文本或 FB2。需 Node.js，首次运行脚本自动安装依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 全书级术语表（glossary）与叙事护照（passport）一次制定、传入每段翻译
- 分段翻译自带评分审查循环（≥9.1 接受 / ≥7.5 修正 / 否则重译，至多十次）
- 审校发现由人工逐条接受，修正仅重跑相关分段，全程变更可撤销
- 支持 Google AI Studio 及任意 OpenAI 兼容服务（含 llama.cpp、LM Studio、Ollama、vLLM 本地服务）

## 适用场景

- 把整本英文小说翻译成中文并保持人名、称谓前后一致
- 用免费 Google key 或本地模型离线完成一本书的翻译
- 对机翻结果逐条审阅审校发现并只重译需要修正的分段
- 导出带封面与目录的 FB2 电子书

## 场景标签

 · 领域:翻译/内容生成

## 证据(README 行号)

> L3: prozetta translates fiction with language models. The text is translated in
> L6: address, the gender of each character. The program runs locally, through a web
> L38: **The part level.** Each part is translated separately. Along with it, the model
> L40: the relevant parts of the passport. A separate model call checks the draft.

## 星数曲线

```mermaid
xychart-beta
    title "UrgenProchnoff/prozetta 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-11-15", "2026-11-21"]
    y-axis "stars" 10 --> 13
    line [11, 12, 12]
```

2026-10-18 11 → 2026-11-21 12（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `400aab82469a` · [字段定义](../../DATASET.md)*
