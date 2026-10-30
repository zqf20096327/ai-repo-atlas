# anpl-code/Deblank

⭐ 23 · Python · MIT · 推送 2026-03-23 · [GitHub](https://github.com/anpl-code/Deblank) · 组织维护

**面向 LLM 的可逆代码压缩服务：去除代码格式省 token，响应端无损还原**

源于 ICSE'26 论文（获 Distinguished Paper Award）的双向代码压缩层：在送入 LLM 前剥离代码中的可选格式（空白、缩进）以降低 token 数，再将模型输出还原为 PEP 8、Google Style 等标准风格。AST 保持不变，实验显示 C 系语言省约 30%、Python 约 9% token，对 Fill-in-the-Middle 任务 Pass@1 影响可忽略。支持 Python/Java/C/C++/C#/JS/TS/Go 八种语言，以 Docker 容器部署，通过 REST API 的 /unformat_code 与 /format_code 两个端点交互，支持纯代码与自然语言混合模式、语言自动推断及格式化失败时的修复回退策略。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- C 系语言约降 30%、Python 约 9% token，AST 不变
- 八种语言支持，双向压缩/还原，平均约 76ms 每次转换
- Docker 部署，REST API 提供两个端点，支持混合文本中的代码块定位
- 格式化失败时可选修复策略（none/on_failure）及 regex 回退

## 适用场景

- 降低代码补全/编辑场景下的 LLM token 成本
- 把混合自然语言与代码块的提示词送入模型前压缩、响应后还原
- 实时推理管线中嵌入无损代码格式转换服务

## 场景标签

 · 领域:LLM 基础设施/开发工具

## 证据(README 行号)

> L12: **Deblank** is a powerful tool designed to optimize LLM efficiency by reducing the token count of source code throu
> L22: Experiments on 10 different models including, DeepSeek-V3, Claude-3.7, and Gemini-1.5, show that removing formattin
> L80: 1. `http://localhost:[port_number]/unformat_code`

## 星数曲线

```mermaid
xychart-beta
    title "anpl-code/Deblank 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `defab3c32dfe` · [字段定义](../../DATASET.md)*
