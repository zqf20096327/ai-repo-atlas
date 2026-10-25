# georgekhananaev/spark-clean

⭐ 51 · Swift · NOASSERTION · 推送 2026-08-16 · [GitHub](https://github.com/georgekhananaev/spark-clean) · [官网](https://github.com/georgekhananaev/spark-clean/releases) · 个人维护

**面向开发者的 macOS 磁盘清理与存储分析应用**

原生 SwiftUI macOS 应用，集缓存清理、存储分析、重复文件查找与应用卸载于一体。针对开发者机器覆盖 Xcode、node_modules、Rust targets、Python 环境、JetBrains、Homebrew、Docker 资源及已安装的 Ollama 模型（经官方 CLI 执行删除）。清理前按 Safe/Review/Caution 风险分级，默认移入废纸篓并可撤销恢复。无账户、订阅、分析与遥测，扫描与清理均在本地进行；采用源码可得许可，个人、教育与非商业用途免费。通过 GitHub Releases 提供 DMG 安装包，另可从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Safe/Review/Caution 三级风险标注与路径级删除限制
- 覆盖 Xcode、Docker、Ollama 模型、多语言包管理等开发者工具链的清理
- 字节级重复文件检测（大小、文件头、SHA-256 三重校验）
- 默认移入废纸篓并支持 Shift+Cmd+Z 恢复上次清理

## 适用场景

- 清理 Xcode DerivedData、node_modules 等可重建的开发缓存释放磁盘
- 通过只读 Disk Map 查明磁盘空间占用分布
- 审查并卸载应用及其关联的缓存、日志与支持数据
- 安全地删除重复文件与旧 Time Machine 本地快照

## 场景标签

 · 领域:系统工具/磁盘清理

## 证据(README 行号)

> L14: SparkClean is a native macOS disk cleaner that combines a cache cleaner, storage
> L48: |Docker and Ollama|Measures reclaimable Docker resources and installed Ollama models, then uses their official CLIs

## 星数曲线

```mermaid
xychart-beta
    title "georgekhananaev/spark-clean 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 49 --> 52
    line [50, 51, 51]
```

2026-10-18 50 → 2026-10-25 51（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `67c9f12276b4` · [字段定义](../../DATASET.md)*
