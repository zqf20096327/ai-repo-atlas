# thebearwithabite/ai-file-organizer

⭐ 50 · Python · MIT · 推送 2026-10-11 · [GitHub](https://github.com/thebearwithabite/ai-file-organizer) · 个人维护

**本地文件自动整理工具：AI 分类并从用户纠正中学习**

面向个人用户（标注 ADHD-friendly）的文件整理系统：通过计算机视觉、音频分析与分块处理对文件分类，设 7 天观察期后再整理，提供 NEVER/MINIMAL/SMART/ALWAYS 四档置信度模式，并可从用户的纠正中自适应学习。附带 3 级去重校验（大小→MD5→SHA256）、回滚系统、磁盘监控与可选 Google Drive 云卸载。以 Python 源码方式运行，通过浏览器访问 localhost:8000 界面，支持插件扩展自定义分类器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 天观察期 + 四档置信度决策模式
- 从用户纠正中自适应学习
- 3 级去重校验（大小→MD5→SHA256）与完整回滚
- 插件系统可扩展自定义分类器

## 适用场景

- 我想让积压的下载/文档文件夹自动归类
- 我想先观察再整理，不确定的文件由我确认
- 我希望整理操作可撤销、避免误删重复文件

## 场景标签

 · 领域:桌面工具/文件管理

## 证据(README 行号)

> L3: An intelligent, ADHD-friendly file organization system that learns from your behavior.
> L9: - **Adaptive Learning** — Learns from your corrections
> L76: Create custom classifiers in `plugins/`. See `plugins/README.md` for the API.

## 星数曲线

```mermaid
xychart-beta
    title "thebearwithabite/ai-file-organizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-25 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 low · 依据 README sha `e8e3dbc75deb` · [字段定义](../../DATASET.md)*
