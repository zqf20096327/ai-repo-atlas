# guangxiangdebizi/PolicyAgents

⭐ 10 · Python · MIT · 推送 2026-11-11 · [GitHub](https://github.com/guangxiangdebizi/PolicyAgents) · 个人维护 · 中文 README

**对政策文本生成四部分分析报告的多 Agent 工具**

基于 LangGraph、LangChain 和可选 MCP 工具的政策文本分析原型：输入政策文本后由三个分析 Agent 并发执行，生成意图与要点、政策空缺、积极影响、消极影响与风险四部分 Markdown 报告。提供 Streamlit 网页界面（粘贴文本或上传 TXT/Markdown、查看运行日志）与 CLI 两种入口，支持 OpenAI 兼容接口及 Anthropic 接口，可导出 Markdown/PDF，运行记录另存 JSON。无在线体验站，启动脚本仅监听 localhost，无多用户认证，不适合直接公开部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 三个分析 Agent 通过 asyncio.gather 并发执行并汇总为固定结构报告
- 按需加载 stdio 或 Streamable HTTP 的 MCP 服务，默认不启用工具
- 网页与 CLI 共用分析函数，运行记录独立保存为 JSON
- 支持 OpenAI 兼容接口与 Anthropic 接口，模型通过 MODEL_CONFIG 配置

## 适用场景

- 研究公开政策文本并整理成结构化分析报告
- 演示 LangGraph 多 Agent 并发工作流的开发实践
- 本地分析政策文本并导出 PDF 报告与运行记录

## 场景标签

`多智能体` `科研工具` · 领域:Agent 开发

## 证据(README 行号)

> L3: 基于 LangGraph、LangChain 和可选 MCP 工具的政策文本分析原型。
> L4: 输入政策文本，分别生成意图与要点、政策空缺、积极影响、消极影响与风险四部分报告。
> L12: - 三个分析 Agent 并发执行，汇总为固定结构的 Markdown 报告。

## 星数曲线

```mermaid
xychart-beta
    title "guangxiangdebizi/PolicyAgents 星数(近 2 点)"
    x-axis ["2026-11-19", "2026-11-22"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-11-19 10 → 2026-11-22 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `05cd491d9ff8` · [字段定义](../../DATASET.md)*
