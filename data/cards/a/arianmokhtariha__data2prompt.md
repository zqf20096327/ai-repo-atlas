# arianmokhtariha/data2prompt

⭐ 27 · Python · MIT · 推送 2026-10-29 · [GitHub](https://github.com/arianmokhtariha/data2prompt) · 个人维护

**把数据类项目编译为单个适配 LLM 上下文文件的 CLI 工具**

面向数据科学工作流 Context Engineering 阶段的 Python CLI：将含 CSV、Excel、SQLite、Parquet、Jupyter notebook 等文件的项目打包为一个 PROMPT.md（或 XML）文件，供 ChatGPT、Claude、Gemini 等模型读取。机制包括：对每张表计算列类型、缺失值与统计量并附抽样行，而非逐行粘贴；--budget 按 token 预算裁剪输出；.env 值不进入输出；同项目输出可复现。限制：Parquet/Feather/Arrow 需可选 pyarrow 依赖。通过 uv/pipx/pip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对 CSV/Excel/SQLite 等按列统计加抽样行摘要，替代逐行粘贴
- --budget 按 token 预算裁剪输出并列出被裁内容
- notebook 清洗与执行顺序检查（乱序/未运行/中断告警）
- .env 值隐藏、数据库只读打开、本地 token 计数不上传

## 适用场景

- 把数据项目打包后粘贴到 ChatGPT/Claude/Gemini 对话中分析
- 控制提示文件大小以匹配模型上下文窗口并稳定 API 成本
- 仅共享数据结构（--schema-only）而不含任何行数据

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L12:  Turn data-heavy projects into LLM context that actually fits.
> L14:  single file that ChatGPT, Claude or Gemini can read: summarized, cleaned,

## 星数曲线

```mermaid
xychart-beta
    title "arianmokhtariha/data2prompt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-31 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `ddbca98bca1f` · [字段定义](../../DATASET.md)*
