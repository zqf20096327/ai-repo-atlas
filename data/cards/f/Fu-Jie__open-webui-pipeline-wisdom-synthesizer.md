# Fu-Jie/open-webui-pipeline-wisdom-synthesizer

⭐ 15 · Python · MIT · 推送 2026-03-22 · [GitHub](https://github.com/Fu-Jie/open-webui-pipeline-wisdom-synthesizer) · 个人维护 · 中文 README

**Open WebUI 的聚合回答重构管道：将多模型汇总输出改写为结构化专家分析报告**

面向 Open WebUI 用户的外部 Pipeline 过滤器：拦截“汇总各模型响应”类聚合请求，解析出原始用户提问与各模型各自的回答，指示汇总模型以“首席分析师”角色执行批判性评估流程，而非简单合并，最终按固定版式输出核心共识、关键分歧、独特洞察与综合建议四段式报告。以单文件 Python 管道组件提供，通过 GitHub Raw 链接一键导入 Open WebUI 的 Pipelines 页签；运行前提是后端已连接 open-webui/pipelines 框架的 runner 环境。提供 Valves 参数控制目标模型、执行优先级、专用汇总模型与解析锚点标记。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动拦截 Open WebUI 的多模型聚合请求并解析原始提问与各模型回答
- 强制汇总模型执行批判性评估而非通用合并
- 输出固定四段结构：核心共识/关键分歧/独特洞察/综合建议
- 单文件管道组件，支持 URL 一键导入，Valves 可配置目标模型与触发词

## 适用场景

- 我在 Open WebUI 里同时问多个模型，想让汇总结果更有结构、能看出分歧
- 团队对比多个模型的回答时需要快速区分共识与分歧点
- 为多模型聚合输出附加统一的专家分析版式

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: An external pipeline filter (Pipeline/Filter) for **Open WebUI** that intercepts multi-model aggregate requests to l
> L9: * **Smart Interception**: Automatically catches Open WebUI's “Summarize various models' responses” requests.

## 星数曲线

```mermaid
xychart-beta
    title "Fu-Jie/open-webui-pipeline-wisdom-synthesizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `497f15f4391f` · [字段定义](../../DATASET.md)*
