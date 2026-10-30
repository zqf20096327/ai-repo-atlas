# dbookstaber/OpenAI_Assist_All_Tools

⭐ 15 · Python · 推送 2026-08-16 · [GitHub](https://github.com/dbookstaber/OpenAI_Assist_All_Tools) · 个人维护

**演示 OpenAI Assistant 全部工具类型的 GUI 示例**

演示型应用：以最小 GUI 运行 OpenAI Assistant，并同时启用其全部工具类型——代码解释器、两个文件（PDF 与 CSV）的检索、以及两个自定义函数（生成随机数与随机字符串，定义于 functions.py，为基础 Assistant 补充此能力）。用户与助手的对话写入 AssistantLog.md，完整 OpenAI 交互（多为 JSON）打印到 STDOUT；创建 Assistant 后将其 ID 存入 .env 以避免重复创建。运行需本地 .env 中的 OPENAI_API_KEY，方式为运行 gui.py。示例中的『核授权码』文件为虚构测试数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同时启用代码解释器、文件检索与自定义函数三类工具
- 两个自定义函数（随机数/随机字符串）为基础 Assistant 补充能力
- 对话记录写入 AssistantLog.md，完整交互打印到 STDOUT
- Assistant ID 存入 .env 避免重复创建

## 适用场景

- 学习 OpenAI Assistant 各工具类型的行为与返回格式
- 调试 Function Calling 与文件检索的组合使用
- 查看完整 JSON 交互日志以了解 API 细节

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L5: This is a simple demonstration of an OpenAI Assistant with all possible Tools enabled.
> L6: The "Tools" are a *Code Interpreter*, two files (one PDF and one CSV) for *Retrieval*, and

## 星数曲线

```mermaid
xychart-beta
    title "dbookstaber/OpenAI_Assist_All_Tools 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `c3644e1a7c9a` · [字段定义](../../DATASET.md)*
