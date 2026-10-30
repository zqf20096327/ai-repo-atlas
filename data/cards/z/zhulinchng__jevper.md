# zhulinchng/jevper

⭐ 19 · Python · Apache-2.0 · 推送 2026-10-07 · [GitHub](https://github.com/zhulinchng/jevper) · [官网](https://zhulinchng.github.io/jevper/) · 个人维护

**在任意 OpenAI 兼容客户端上实现 Decisions/分类问答的 Python 封装库**

独立实现 OpenAI Decisions API schema 与 TypeSafe System One 线格式（声明与两者无隶属关系）的 Python 库。开发者传入任意暴露 responses/chat.completions/messages.create 的客户端对象，即可对文本提出 Noul（是/否）、Choice（多选）、Score（量表）三类分类问题，返回带概率与置信度的类型化答案。读取方式有 logprobs、grammar、structured、discrete 四种，默认 auto 按模型与接口自动切换；支持推理配置、few-shot 示例、并发提问。唯一运行时依赖为 pydantic>=2.7，需 Python 3.10+。schema 中不支持的输入（如 input_image）会在发送前拒绝。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三类类型化问题（Noul/Choice/Score）返回概率与置信度
- 不导入任何 provider SDK，任何 OpenAI 兼容客户端对象均可作后端
- 四种 elicitation 方法，auto 按模型/接口记忆性地在 logprobs 与 JSON 间切换
- 对部分实现不完整的服务器自动丢弃被拒字段并重试

## 适用场景

- 在本地 llama.cpp/ollama/vLLM 等无 Decisions 路由的模型上运行同 schema 的分类问答
- 先在现有端点写好决策请求，未来切换官方 Decisions 路由只换客户端
- 对文本/多选项/量表评估任务获取带概率分布而非单一答案的输出

## 场景标签

 · 领域:LLM 基础设施/分类

## 证据(README 行号)

> L13: `usage` for the call. jevper speaks that schema over any model and any OpenAI-compatible surface, so the
> L41: are independent: neither imports the other, and jevper imports no provider SDK at all — any object exposing
> L42: `responses.create`, `chat.completions.create` or `messages.create` works as the client. It is the call the

## 星数曲线

```mermaid
xychart-beta
    title "zhulinchng/jevper 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `c5829cdc3b90` · [字段定义](../../DATASET.md)*
