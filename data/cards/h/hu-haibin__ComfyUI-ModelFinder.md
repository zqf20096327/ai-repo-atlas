# hu-haibin/ComfyUI-ModelFinder

⭐ 46 · Python · 推送 2026-07-19 · [GitHub](https://github.com/hu-haibin/ComfyUI-ModelFinder) · 个人维护 · 中文 README

**扫描 ComfyUI 工作流查找缺失模型的旧版 Python 工具**

Python/Tkinter 编写的独立工具：扫描 ComfyUI 工作流 JSON 提取引用的模型名，与本地 models 目录比对，通过浏览器自动化（依赖 Chrome）搜索缺失模型文件，生成本地结果报告，并支持将下载的模型文件移动整理到 ComfyUI 模型目录。面向能自行管理 Python 环境与 ComfyUI 目录的用户，仅支持 Windows。仓库自述为遗留实现，新的启动、修复与下载功能已转移至维护中的 Wonderful Launcher 桌面应用，本仓库不再提供打包安装器，搜索结果依赖公开搜索页面，可能不完整或有噪声。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 扫描工作流 JSON 并与本地 models 目录比对找出缺失模型
- 浏览器自动化搜索缺失模型文件（依赖 Chrome）
- 生成本地结果报告并整理模型文件到 ComfyUI 目录

## 适用场景

- 排查 ComfyUI 工作流因缺模型而报错的问题
- 整理散落的模型文件到正确的 ComfyUI 子目录

## 场景标签

 · 领域:AI 绘图工具链

## 证据(README 行号)

> L23: ComfyUI-ModelFinder is a legacy open-source Python/Tkinter tool for finding missing ComfyUI models. It can help you
> L25: - scan ComfyUI workflow JSON files and extract referenced model names

## 星数曲线

```mermaid
xychart-beta
    title "hu-haibin/ComfyUI-ModelFinder 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-30 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b8005d7a9889` · [字段定义](../../DATASET.md)*
