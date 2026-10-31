# SoulKyu/leandro

⭐ 15 · Python · MIT · 推送 2026-10-06 · [GitHub](https://github.com/SoulKyu/leandro) · 个人维护

**AI SRE agent：自动诊断 Kubernetes 事件并通过 Google Chat 协作**

运行于 NixOS VM（libvirt/KVM）上的 SRE agent，基于 Hermes 加三个补丁。只读监听 K8s Warning 事件与 pod 相位，事件去重合并后交 LLM 一次性诊断，产出单行结论与可复制的 kubectl 命令，送达 Google Chat；同一 persona 支持 DM/空间对话、50+ 斜杠命令。模型可选 Claude（claude-agent-sdk）或任意 OpenAI 兼容端点。安全设计以提示注入为前提：双只读访问、工具硬禁用名单（fail-closed 基线哈希守卫）、双层默认拒绝出站、出口前正则脱敏、记忆写入需人工批准。部署需 Nix + libvirt/KVM + virt-install，运维全部经 SSH，无入站网络。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 事件按 (namespace, workload, reason) 去重合并，LLM 不可达时仍交付仅事实报告
- 七层模型外强制安全边界：双只读 RBAC/MCP、工具禁用名单、nftables 默认拒绝出站、脱敏、记忆审批
- 20 向量红队提示注入载荷作为回归测试，单 FAIL 阻断部署
- 支持 Claude 与 OpenAI 兼容端点两种可互换模型变体

## 适用场景

- 团队在 Google Chat 中获得 pod 事件的自动诊断与 kubectl 建议
- 以对话方式对集群事件做交互式排查与后续追踪
- 在需审计边界的环境中部署读取攻击者可影响文本的 agent

## 场景标签

 · 领域:云原生运维/AI Agent

## 证据(README 行号)

> L5: An AI SRE teammate that watches a Kubernetes cluster, diagnoses pod
> L31: - **Diagnosis**: each new incident becomes a `hermes -z` one-shot with the
> L13: Two interchangeable model variants: Claude (via `claude-agent-sdk`) or any

## 星数曲线

```mermaid
xychart-beta
    title "SoulKyu/leandro 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `fab6596edb40` · [字段定义](../../DATASET.md)*
