# yurijmikhalevich/rtag

⭐ 17 · Python · MIT · 推送 2026-03-15 · [GitHub](https://github.com/yurijmikhalevich/rtag) · 个人维护

**命令行照片自动打标签工具，基于 CLIP 生成图像标签**

基于 rclip、使用 OpenAI CLIP 神经网络的命令行照片打标签工具：对当前目录及子目录的所有 JPG 图片生成标签，标签从 imagenet-1k 标签列表中选取并写入图像元数据，格式兼容多数照片管理软件。支持自定义标签文件与置信度阈值过滤，可用 --dry-run 查看各标签置信分。项目声明处于活跃开发期，可能存在 bug 与变更。需 Python 与 Poetry 从源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 对目录及子目录 JPG 图片批量生成标签并写入元数据
- 使用 OpenAI CLIP 神经网络，默认 imagenet-1k 标签列表
- 支持自定义标签文件与 --threshold 置信度过滤
- --dry-run 模式查看各标签置信分

## 适用场景

- 批量给照片库打标签以便照片管理软件检索
- 用自定义标签体系整理图片集
- 打标签前用 dry-run 预览置信度结果

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L5: **rtag** is a command-line photo tagging tool based on rclip and powered by the awesome OpenAI's CLIP neural network
> L10: subdirectories, with the most relevant tags out of the imagenet-1k tag list. **rtag** writes the tags to the

## 星数曲线

```mermaid
xychart-beta
    title "yurijmikhalevich/rtag 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `804ef331566d` · [字段定义](../../DATASET.md)*
