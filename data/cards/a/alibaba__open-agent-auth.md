# alibaba/open-agent-auth

⭐ 83 · Java · Apache-2.0 · 推送 2026-03-15 · [GitHub](https://github.com/alibaba/open-agent-auth) · [官网](https://alibaba.github.io/open-agent-auth/) · 组织维护 · 中文 README

**企业级 AI Agent 操作授权框架，实现身份绑定与细粒度鉴权**

基于 IETF 草案 draft-liu-agent-operation-authorization-01 的 Java/Spring Boot 授权框架，面向代表用户执行操作的 AI Agent 场景：三层密码学身份绑定（ID Token→WIT→AOAT）、请求级虚拟工作负载隔离（WIMSE 模式、临时密钥）、细粒度动态策略评估（OPA/RAM/ACL，运行时可更新）、基于 W3C VC 的语义审计。基于 OAuth 2.0/OIDC/MCP 协议构建。当前处于 public beta（v0.1.0-beta.1），artifacts 尚未发布到 Maven Central，需本地构建安装；示例提供 Mock LLM 与 QwenCode 两种启动方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 三层密码学身份绑定（ID Token → WIT → AOAT）
- 请求级虚拟工作负载隔离与临时凭证（WIMSE 模式）
- 动态策略注册（OPA/RAM/ACL），运行时更新无需重启
- 基于 W3C VC 的语义审计轨迹

## 适用场景

- 为企业内代表用户执行操作的 AI Agent 提供授权与审计
- 需要将每次 Agent 操作追溯到用户显式授权的场景
- 对 Agent 资源访问做细粒度、可动态调整的权限控制

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L20: Open Agent Auth is an enterprise-grade authorization framework that provides cryptographic identity binding, fine-g
> L22: The framework is implemented based on IETF Draft: Agent Operation Authorization (draft-liu-agent-operation-authoriz

## 星数曲线

```mermaid
xychart-beta
    title "alibaba/open-agent-auth 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 80 --> 83
    line [81, 82, 82]
```

2026-10-18 81 → 2026-10-25 82（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `f89fe05a7b63` · [字段定义](../../DATASET.md)*
