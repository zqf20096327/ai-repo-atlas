# netboxlabs/netbox-agent-compliance

⭐ 22 · Python · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/netboxlabs/netbox-agent-compliance) · 组织维护

**用自然语言规则对 NetBox 做合规检查的 AI agent 示例**

基于 OpenAI Agents SDK、LiteLLM 与 NetBox MCP server 构建的合规检查 agent：用户以英文自然语言书写规则（如“每个接口应有 IP”），按 site/rack/device 范围执行只读检查，仅支持映射到 NetBox 核心数据模型的规则。通过 LiteLLM 可选 OpenAI 或 Anthropic 模型，默认 openai/gpt-5-nano。代码约 150 行，官方定位为构建自有 NetBox agent 的示例。限制：约 25 次工具调用软上限、不支持自定义字段与插件数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言合规规则，按 site/rack/device 范围检查
- 经 LiteLLM 支持 OpenAI 与 Anthropic 模型，默认 gpt-5-nano
- 只读操作，约 150 行的最小实现
- 四模块结构：CLI、agent 编排、prompts、MCP stdio 辅助

## 适用场景

- 检查站点内所有接口是否分配了 IP 地址
- 检查机柜内设备是否配置主 IPv4/IPv6
- 作为参考示例开发自己的 NetBox agent

## 场景标签

 · 领域:网络基础设施管理/运维

## 证据(README 行号)

> L3: A lean agent that performs NetBox compliance checks using natural language rules. Built with OpenAI Agents SDK, Lite
> L13: - **Model agnostic** - Works with OpenAI or Anthropic models via LiteLLM
> L65: netbox-agent-compliance "every interface should have an assigned ip address" --site "NYC"

## 星数曲线

```mermaid
xychart-beta
    title "netboxlabs/netbox-agent-compliance 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `b1cbbaa98808` · [字段定义](../../DATASET.md)*
