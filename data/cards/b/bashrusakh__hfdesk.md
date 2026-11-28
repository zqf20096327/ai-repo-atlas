# bashrusakh/hfdesk

⭐ 10 · Go · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/bashrusakh/hfdesk) · [官网](https://github.com/bashrusakh/hfdesk/releases) · 个人维护

**本地 Hugging Face 模型搜索、分析与下载管理仪表盘**

以单个静态二进制提供的本地 Web 仪表盘：在浏览器中搜索 Hugging Face Hub 的模型与数据集，下载前查看仓库内容（量化版本、文件分组、内存估算、推荐选项），支持并行断点续传与任务跟踪，可浏览本地 HF 缓存并将模型镜像到 NAS、USB 或其他机器。缓存布局兼容标准 HF cache 或 LM Studio 风格目录，提供代理、基础认证、服务模式（systemd/launchd/Windows 服务）与本地 JSON API。Windows 桌面版含托盘图标与服务管理。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 下载前查看仓库量化版本、文件分组、RAM 估算与推荐选项
- 并行断点续传下载，带进度、重试与任务跟踪
- 缓存浏览器并支持镜像到 NAS、USB 或其他机器
- 单一静态二进制，兼容 HF cache 与 LM Studio 风格目录

## 适用场景

- 批量下载和管理本地 Hugging Face 模型文件
- 下载前检查仓库内容与量化版本再决定拉取
- 在 NAS 或家庭服务器上镜像模型库
- 用 Windows 服务在后台持续跑下载任务

## 场景标签

 · 领域:模型管理工具/开发工具

## 证据(README 行号)

> L7: **A local web dashboard for finding, analyzing, downloading, and managing
> L10: Start HFDesk and it opens in your browser: search the Hub, inspect a
> L11: repository before pulling it, download with resume, browse your local cache,


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `8d26f1efdcd2` · [字段定义](../../DATASET.md)*
