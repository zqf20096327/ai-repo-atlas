# NosytLabs/skillstate-proxy

⭐ 30 · TypeScript · MIT · 推送 2026-10-23 · [GitHub](https://github.com/NosytLabs/skillstate-proxy) · [官网](https://www.npmjs.com/package/skillstate-proxy) · 组织维护

**本地 LLM 代理：用结构化会话状态替代重放历史上下文**

面向 agent 工作流的本地 HTTP 代理，位于客户端与配置的上游模型提供商之间：从任务规格、会话 JSON 状态与最新观测构造上下文，并从模型响应中提取 state_patch 合并回状态，后续请求基于保留状态而非完整转录重放。提供 OpenAI 格式（/v1/chat/completions）与 Anthropic 格式（/v1/messages）翻译路径，可选每上游 rpm/tpm 本地限流与 /cost 成本汇总。README 明确声明节省额、延迟、准确性与兼容性均不保证，非无损转录存档，需 Node.js 20+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- state_patch 合并机制：数组替换、对象递归合并、null 删除键
- OpenAI 与 Anthropic 双格式 HTTP 接口及模型列表转发
- 本地一分钟滚动窗口 rpm/tpm 限流与 /cost 成本记录
- npm 全局安装，CLI 与环境变量/配置文件三层配置优先级

## 适用场景

- 长程 agent 任务中减少重复发送历史上下文
- 让现有 OpenAI/Anthropic 兼容客户端无需改动接入状态压缩代理
- 本地跟踪会话状态与成本汇总

## 场景标签

`模型网关` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L9: The proxy sits between a client and a configured model provider. It builds context from the task specification, the 
> L31: The default listener is `127.0.0.1:8789`. A compatible chat client uses `http://127.0.0.1:8789/v1` as its API base 

## 星数曲线

```mermaid
xychart-beta
    title "NosytLabs/skillstate-proxy 星数(近 2 点)"
    x-axis ["2026-10-28", "2026-10-31"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-28 30 → 2026-10-31 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `42f0fb88d311` · [字段定义](../../DATASET.md)*
