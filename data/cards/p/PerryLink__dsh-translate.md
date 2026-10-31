# PerryLink/dsh-translate

⭐ 14 · JavaScript · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/PerryLink/dsh-translate) · [官网](https://perrylink.github.io/plugins/dsh-translate/) · 个人维护 · 中文 README

**DeepSeek Harness 插件：跨 11 家厂商参数映射与确定性 JSON 修复**

面向 DeepSeek Harness（DSH）的纯 JS 宿主插件，提供两个独立面：/translate 命令将 temperature、top_p、max_tokens 等 13 个标准参数在 11 家厂商（OpenAI、ERNIE、Qwen、Anthropic 等）间做查表式映射；修复层通过 tools/post-execute 监听器与 fix_json 工具，对工具输出中的破损 JSON 做确定性修复（围栏提取、转义修复、尾逗号移除、截断闭合、必填字段补 null），不编造任何值，不可修复则保持原样。支持 JSON Schema 子集有限（type/oneOf/properties 等），无需网络、子进程或凭证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- /translate 覆盖 11 家厂商 × 13 个标准参数的成对映射与整请求转换
- post-execute 修复层含围栏提取、转义修复、尾逗号移除、截断闭合、补 null 占位
- 修复为确定性文本手术，不调用模型、不编造值，不可修复即 fail closed
- 无网络/无子进程/无凭证，仅消费宿主 commands 与 tools 服务

## 适用场景

- 跨厂商迁移或对照 LLM 请求参数时查询映射表
- agent 工具输出 JSON 被截断或格式破损时自动修复
- 在 DeepSeek Harness 中按 schema 校验并修复工具结果

## 场景标签

 · 领域:LLM 工具链/开发者工具

## 证据(README 行号)

> L7: **Vendor parameter translation and deterministic JSON repair for DeepSeek Harness.**
> L69: - **`/translate`** — the vendor parameter translation table: `temperature`, `top_p`, `max_tokens`, `stop`, `system`
> L70: - **The repair layer** — a `tools/post-execute` listener plus the `fix_json` tool. When a successful tool result ca

## 星数曲线

```mermaid
xychart-beta
    title "PerryLink/dsh-translate 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `f548598aaad5` · [字段定义](../../DATASET.md)*
