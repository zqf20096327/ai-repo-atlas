# HaiTrung-Workspace/tidymint

⭐ 9 · Swift · MIT · 推送 2026-11-22 · [GitHub](https://github.com/HaiTrung-Workspace/tidymint) · [官网](https://tidymint.app) · 个人维护

**面向 AI 工具使用者的开源 Mac 清理工具**

macOS 14+ 的免费开源清理工具，核心机制是所有清理动作先移入废纸篓并可撤销，删除重复文件前检查项目文件夹并标记仍被脚本引用的文件。功能覆盖缓存/日志扫描清理、按应用清理（含 Ollama/Hugging Face/LM Studio 本地模型逐行列出）、SHA-256 重复文件查找、气泡图磁盘分析、应用卸载、大文件管理，并内置窗口平铺（Mintangle）、文件暂存架（Mintdrop）与菜单栏整理（Mintbar）。提供 Apple silicon 与 Intel 版下载、Homebrew 与源码构建；Mint 工具源码不在仓库内。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 所有清理先入废纸篓，可撤销删除操作
- 本地 AI 模型（Ollama、Hugging Face、LM Studio）逐模型列出清理
- SHA-256 重复文件检测，删除前检查项目文件夹引用
- 扫描与清理完全本地离线运行

## 适用场景

- 清理 AI 工作留下的模型文件、缓存与重复素材
- 卸载应用并清除残留文件
- 可视化查看磁盘空间占用分布
- 清理长期未动的 node_modules 与 Python 环境

## 场景标签

 · 领域:系统工具/macOS 清理

## 证据(README 行号)

> L7: **Keep your Mac in mint condition.** A free, open-source Mac cleaner, built for people who work with AI tools. A fre
> L9: AI work leaves a lot behind: model files, drafts, exported images, duplicate assets, caches from browsers and editor

## 星数曲线

```mermaid
xychart-beta
    title "HaiTrung-Workspace/tidymint 星数(近 3 点)"
    x-axis ["2026-11-10", "2026-11-15", "2026-11-24"]
    y-axis "stars" 7 --> 10
    line [8, 9, 9]
```

2026-11-10 8 → 2026-11-24 9（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `93bb60bc9109` · [字段定义](../../DATASET.md)*
