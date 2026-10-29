# huggingface/hub-sync

⭐ 23 · Apache-2.0 · 推送 2026-08-31 · [GitHub](https://github.com/huggingface/hub-sync) · 组织维护

**把 GitHub 仓库同步到 Hugging Face Hub 的 GitHub Action**

由 Hugging Face 维护的 GitHub Action：通过官方 HF CLI（以 uvx 运行）将 GitHub 仓库内容部署到 Hugging Face 的 Spaces、Models 或 Datasets。同步采用镜像模式，默认删除 Hub 侧已过滤或不存在的文件，可设 delete_removed: false 仅上传不删除；内置不可关闭的 .git/.github 排除规则，支持用户自定义 include/exclude 的 fnmatch 模式、子目录同步（适用于 monorepo），同步提交信息标识来源 GitHub 仓库。

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

- 同步到 Hugging Face Spaces / Models / Datasets
- 镜像模式默认删除 Hub 侧多余文件，可关闭删除仅上传
- fnmatch 的 include/exclude 过滤规则与子目录同步
- 同步提交标识来源 GitHub 仓库

## 适用场景

- push 代码时自动将模型或数据集仓库镜像到 Hugging Face Hub
- monorepo 中只同步指定子目录到 Hub
- 与 CI 配合在训练后仅追加文件而不删除 Hub 内容

## 场景标签

 · 领域:开发工具/CI 集成

## 证据(README 行号)

> L3: A GitHub Action that syncs your repository to Hugging Face Hub 🤗
> L5: Uses the official HF CLI via `uvx` to deploy to Spaces, Models, or Datasets.

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/hub-sync 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-29"]
    y-axis "stars" 21 --> 24
    line [22, 23, 23]
```

2026-10-18 22 → 2026-10-29 23（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `6d3a2532530a` · [字段定义](../../DATASET.md)*
