# knowsuchagency/struct-gpt

⭐ 31 · Python · MIT · 推送 2026-10-12 · [GitHub](https://github.com/knowsuchagency/struct-gpt) · [官网](https://pypi.org/project/struct-gpt/) · 个人维护

**从 LLM 获取结构化输出的 Python 库，基于 Pydantic 校验**

基于 OpenAI API 与 Pydantic 的 Python 库：开发者定义 Pydantic 模型类，通过 from_openai 让 LLM 返回符合 schema 的结构化数据，自动校验与序列化。支持模板变量、类间引用、重试与温度配置、JSON mode（默认开启，可关闭）、传入示例提升可靠性。默认模型 gpt-4o-mini，需 openai>=1.0，可通过 client 参数接入 AzureOpenAI 或自定义 base_url。

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

- Pydantic 模型定义 + LLM 结构化输出与校验
- 默认启用 JSON mode，可传 json_mode=False 关闭
- 重试与温度配置、传入示例提升准确性
- 支持 AzureOpenAI 或自定义 base_url 的 client

## 适用场景

- 让 LLM 返回符合 Pydantic schema 的可校验数据
- 给已有 Pydantic 类通过 OpenAiMixin 增加结构化生成能力
- 用少量示例引导模型提升输出可靠性

## 场景标签

 · 领域:LLM 开发库

## 证据(README 行号)

> L6: Get structured output from LLM's.
> L23: * Easy creation of custom models using the OpenAI API
> L36: * Requires `openai>=1.0`. By default `from_openai` builds an `openai.OpenAI()` client, which reads `OPENAI_API_KEY`

## 星数曲线

```mermaid
xychart-beta
    title "knowsuchagency/struct-gpt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-28 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `c86d389e3ba3` · [字段定义](../../DATASET.md)*
