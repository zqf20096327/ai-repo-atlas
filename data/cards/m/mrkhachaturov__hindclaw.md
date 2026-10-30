# mrkhachaturov/hindclaw

⭐ 22 · Python · NOASSERTION · 推送 2026-08-25 · [GitHub](https://github.com/mrkhachaturov/hindclaw) · 个人维护

**自托管 Hindsight 记忆管理平台：多租户权限与 Terraform 基础设施**

构建于 Hindsight agent 记忆引擎之上的自托管管理平台，面向需要在生产环境为多个用户和 agent 运行长期记忆的运维者/团队。提供服务端访问控制（三个 Hindsight 扩展负责认证、权限校验与管理 API）、用户/组权限级联（全局默认→组→bank 组→bank 用户逐级覆盖）、跨 agent 并行召回、命名 retain 策略，以及 Terraform provider 将用户、组、bank、权限、指令、心智模型纳入基础设施即代码。通过 npm 插件安装到 OpenClaw 网关，设置 jwtSecret 后自动拉起内嵌 Hindsight daemon。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三个服务端 Hindsight 扩展（Tenant/Validator/Http）实现认证、逐用户逐 bank 权限与 REST 管理 API
- Terraform provider 管理用户、组、权限、bank 配置、指令与心智模型
- 零配置嵌入模式：插件自动启动 Hindsight daemon 并安装扩展
- 跨 agent 并行召回多 bank，按 bank 校验权限

## 适用场景

- 生产环境中为多用户多 agent 的 Hindsight 记忆做权限管理
- 用 Terraform 声明式管理记忆系统的用户、组与策略
- 从 @vectorize-io/hindsight-openclaw 迁移（bank ID 兼容，记忆保留）

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: Self-hosted Hindsight management platform — multi-tenant access control, user/group
> L6: permissions, Terraform-managed infrastructure, and client integrations for AI agent memory.

## 星数曲线

```mermaid
xychart-beta
    title "mrkhachaturov/hindclaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-30 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `62f0259af08a` · [字段定义](../../DATASET.md)*
