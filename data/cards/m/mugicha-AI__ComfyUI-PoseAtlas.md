# mugicha-AI/ComfyUI-PoseAtlas

⭐ 20 · Python · NOASSERTION · 推送 2026-10-29 · [GitHub](https://github.com/mugicha-AI/ComfyUI-PoseAtlas) · 个人维护 · 中文 README

**ComfyUI 姿态参考图库节点：288 组多角度人台线稿可视化选用**

把 RuiC-PoseAtlas 静态姿态图库封装为 ComfyUI 节点：PoseAtlasLoader 提供全屏图库面板（4 系列、26 子分类、中英日搜索、5 角度切换），选中后输出 IMAGE/MASK；PoseAtlasInfo 输出姿态名称等文字信息供拼提示词。仓库不含图片，需运行脚本从原作者仓库下载（约 660 MB，多镜像自动切换续传），图片版权归原作者、禁止再分发。面向用 ControlNet 或图生图/编辑模型做 AI 绘画的创作者，示例工作流配合 Flux3 Klein、Qwen-Image 2.1 使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 1439 项下拉框替换为全屏图库面板，支持中/英/日名称与编号搜索
- 两个节点：PoseAtlasLoader 输出 IMAGE/MASK，PoseAtlasInfo 输出姿态名称/分类/系列
- 下载脚本在 6 个镜像间自动切换，支持断点续传与仅缩略图模式（约 22 MB）
- 提供 3 个示例工作流（含 Flux3 Klein 与 Qwen-Image 2.1 编辑链路）

## 适用场景

- AI 绘画时在 ComfyUI 内直接挑选人体姿态参考线稿
- 配合 ControlNet 抽骨架控制生成图像的姿势与镜头角度
- 把姿态线稿作为参考图喂图生图/编辑模型，保留姿态重绘外观

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: 把 RuiC-PoseAtlas 的 **288 组人体姿态 / 1439 张多角度人台线稿** 做成了 ComfyUI 节点。
> L96: 拖一个 **PoseAtlas 姿态图库**，点「打开图库」选一张，`image` 输出接到任何吃 `IMAGE` 的节点。
> L155: 这个节点本身很轻（只读图，不跑模型），但配套的 ControlNet / 编辑模型需要显存。


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `b62380830ecd` · [字段定义](../../DATASET.md)*
