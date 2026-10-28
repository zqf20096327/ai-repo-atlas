# Pyenb/Ollama-models

⭐ 96 · Shell · GPL-3.0 · 推送 2025-11-02 · [GitHub](https://github.com/Pyenb/Ollama-models) · [官网](https://data.pyenb.network/Github/Ollama/models/) · 个人维护

**Ollama 模型离线分发仓库：下载解压即用**

为无法联网的机器提供 Ollama 模型文件的打包分发：收录 codellama、llama3.x、gemma2、qwen、mistral 等 20 余个模型（1B–70B 参数规模），以 .tar.gz 形式经 Storage VPS 或 Torrent 下载，解压后放入 .ollama/models 目录即可离线运行。另附 ollama-exporter.sh 脚本（Linux、WIP）用于自行从 Ollama registry 导出任意模型。README 顶部声明仓库长期未更新、恢复时间无 ETA；文件声明仅供教育/研究用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 20 余个 Ollama 模型（1B–70B）的离线打包下载
- 提供 VPS 直链与 Torrent 两种下载渠道
- ollama-exporter.sh 脚本支持从 registry 自行导出模型
- 解压放入 .ollama/models 后 ollama run 直接离线运行

## 适用场景

- 为无网络环境的机器离线安装 Ollama 模型
- 获取registry 中已下架或难拉取的模型文件
- 打包备份自己已有的 Ollama 模型

## 场景标签

 · 领域:LLM 模型分发

## 证据(README 行号)

> L8: This repository fulfills a simple purpose: to provide models for ollama to machines that are not connected to the in
> L28: |Model|Parameters|Last Modified|Size|Download Links|

## 星数曲线

```mermaid
xychart-beta
    title "Pyenb/Ollama-models 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-28"]
    y-axis "stars" 94 --> 97
    line [95, 96, 96]
```

2026-10-18 95 → 2026-10-28 96（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `25f1d70bafc7` · [字段定义](../../DATASET.md)*
