# coder/registry

⭐ 82 · HCL · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/coder/registry) · [官网](https://registry.coder.com) · 组织维护

**发布与发现 Coder 工作区 Terraform 模块的社区注册平台**

面向 Coder 用户的社区驱动注册平台：开发者将可复用的 Terraform 封装为 Coder Modules 发布，供全球用户扩展其远程开发工作区。平台基于 HashiCorp 开源的 Terraform 语言，通过 import 片段接入 JetBrains、Cursor、VS Code 等开发工具集成；官网为仓库的完整镜像，提供 .tar 资源下载。外部 PR 需满足基线要求才可发布，仅 `verified` 标记的资源由 Coder 背书，Coder 命名空间下模块自动验证。Templates 支持将在后续数周内加入，官方模板暂存于 coder/coder 仓库 examples/templates 目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 Terraform 模块形式发布可复用的工作区扩展
- import 片段即可将模块集成进 Coder 模板
- 官网为仓库完整镜像，提供 .tar 资源下载
- verified 状态标记机制，Coder 命名空间模块自动验证

## 适用场景

- 为我的 Coder 远程开发工作区查找现成集成模块（如 Cursor、JetBrains）
- 把自己写的 Terraform 集成发布给其他 Coder 用户复用
- 浏览社区与官方维护的工作区扩展生态

## 场景标签

 · 领域:开发工具/基础设施

## 证据(README 行号)

> L7: Coder Registry is a community-driven platform for extending your Coder workspaces. Publish reusable Terraform as Cod
> L14: Coder is built on HashiCorp's open-source Terraform language to provide developers an easy, declarative way to defi

## 星数曲线

```mermaid
xychart-beta
    title "coder/registry 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 80 --> 83
    line [81, 82, 82]
```

2026-10-18 81 → 2026-10-28 82（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `336335a42b37` · [字段定义](../../DATASET.md)*
