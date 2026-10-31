# smaramwbc/statewave-grounded-shop-assistant

⭐ 14 · TypeScript · Apache-2.0 · 推送 2026-10-16 · [GitHub](https://github.com/smaramwbc/statewave-grounded-shop-assistant) · 组织维护

**Statewave 记忆运行时的落地示例：带引用的商店问答与内容缺口闭环**

以虚构园艺商店为场景的可运行 TypeScript 演示：面向顾客的问答助手只基于检索到的证据（Episode→编译 Subject→getContext）作答并附经验证的引用，无证据时明示不知道并自动写入 Coverage gap；内部 Ops Assistant 读取缺口、商品目录与 FAQ，供内容团队排查与闭环解决。默认零配置、无 API key 的确定性离线应答，也可配置 OpenRouter 或任意 OpenAI 兼容网关（含自托管 LiteLLM + 本地 Ollama）获得真实 LLM 回答。README 明确其为 demo：db.json 单文件存储、内存会话、单进程限流，不适于多实例生产。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 答案必须基于检索证据，引用 ID 会与实际检索证据比对验证
- 无法作答时自动记录 Coverage gap，Ops Assistant 读取并支持闭环解决
- append-only 记忆：更新以同 sourceId 追加新 Episode，编译时保留最新
- 默认离线规则应答，零设置无 API key；可选 OpenRouter/LiteLLM 网关

## 适用场景

- 端到端查看 Statewave Episode→Subject→grounded completion→引用解析的集成模式
- 为电商/客服场景搭建有引用、不编造的问答助手原型
- 体验内容缺口自动记录与内容团队闭环修复流程

## 场景标签

`聊天机器人` `RAG` · 领域:对话与助手

## 证据(README 行号)

> L9: A runnable use case for **Statewave**: a grounded product advisor and support
> L13: Every answer the shopper-facing assistant gives is grounded in retrieved
> L18: The whole demo runs **with zero setup and no API key**, using a deterministic

## 星数曲线

```mermaid
xychart-beta
    title "smaramwbc/statewave-grounded-shop-assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `63edcde5dc66` · [字段定义](../../DATASET.md)*
