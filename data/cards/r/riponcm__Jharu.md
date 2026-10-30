# riponcm/Jharu

⭐ 79 · Rust · Apache-2.0 · 推送 2026-07-24 · [GitHub](https://github.com/riponcm/Jharu) · [官网](https://jharu.matily.org) · 个人维护

**面向开发者的开源磁盘清理与空间分析桌面应用**

基于 Tauri（Rust 扫描器 + React UI）的 macOS/Windows 磁盘清理应用，面向软件开发者与机器学习工程师。内置已知缓存与数据位置的知识库，扫描 Hugging Face、Ollama、PyTorch、Whisper 等 ML 模型缓存及 npm/pip/conda/Docker 等 25+ 开发者缓存位置，对每项给出安全等级与陈旧度，清理动作一律移入回收站而非永久删除；可区分已加载与从未加载的模型。另含深度清理 treemap、应用卸载残留清理、浏览器缓存和驱动器 SMART 状态。限制：应用未付费签名，首次打开有系统警告。

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

- 扫描 25+ 开发者与 ML 缓存位置，含逐项安全等级与陈旧度检测
- 区分实际加载过与从未加载的 ML 模型；Ollama 共享层保留以免破坏其他模型
- 所有清理动作移入回收站，系统位置受保护不可清理
- 应用卸载器（Windows 读注册表）与全盘 treemap 分析、驱动器 SMART/容量预测

## 适用场景

- 下载大量 ML 模型后磁盘占满，找出从未加载过的模型并回收空间
- 查看 npm/pip/conda/Docker 等开发缓存占了多少磁盘并安全清理
- 卸载应用时连残留配置、缓存与支持文件一并清除
- 分析整块磁盘空间去向，区分系统文件、应用与开发者数据

## 场景标签

 · 领域:开发者工具/磁盘清理

## 证据(README 行号)

> L30: Jharu is a desktop disk cleanup app built specifically for software developers and machine learning engineers. Gene
> L65: Every downloaded model listed individually, across Hugging Face, Ollama, Whisper, PyTorch and Keras. Jharu distingu

## 星数曲线

```mermaid
xychart-beta
    title "riponcm/Jharu 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 78 --> 80
    line [79, 79]
```

2026-10-18 79 → 2026-10-30 79（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 low · 依据 README sha `8d599f539325` · [字段定义](../../DATASET.md)*
