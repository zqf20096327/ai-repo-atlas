# Xz3r0-M/ComfyUI-Xz3r0-Nodes

⭐ 18 · JavaScript · GPL-3.0 · 推送 2026-10-29 · [GitHub](https://github.com/Xz3r0-M/ComfyUI-Xz3r0-Nodes) · [官网](https://xz3r0-m.github.io/ComfyUI-Xz3r0-Nodes/) · 个人维护 · 中文 README

**ComfyUI 自定义节点集：工作流基础功能节点与多媒体数据中枢 XDataHub**

面向 ComfyUI 工作流使用者的自定义节点包，覆盖三大节点组：文件处理（XVideoSave/XAudioSave 等保存与加载节点）、工作流处理（列表/管道/字符串/预览等 26 个工具节点）、XDataHub（图像/视频/音频/LoRA 的预览与加载中心）。界面支持中英文，输入文件名与路径做了防遍历攻击处理。视频/音频保存与缩略图功能依赖系统安装的 FFmpeg。提供 ComfyUI-Manager 一键安装、手动 git clone 安装与在线网页版，仅在 Windows 11 上测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三大节点组：文件处理、工作流处理（26 个节点）、XDataHub
- XDataHub 提供图像/视频/音频/LoRA 的预览与加载
- 中英文多语言节点界面
- 文件名/路径防遍历攻击处理

## 适用场景

- 在 ComfyUI 工作流中保存/加载视频、音频、图像与 LoRA 文件
- 用工作流工具节点简化列表、管道与字符串操作
- 通过 XDataHub 集中浏览和加载多媒体素材

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L14: - 提供许多 ComfyUI 工作流都需要的人性化基础功能节点，让工作流用起来更快捷、搭起来更简洁。并提供多媒体文件（图像 / 视频 / 音频 / LoRA）的预览和加载中心 XDataHub。
> L67: ||XAnyGate10|XAnyToString|XAudioProcess|XController|XControlPanel|XDateTimeString|XImageCompare|XImagePreview|XImag

## 星数曲线

```mermaid
xychart-beta
    title "Xz3r0-M/ComfyUI-Xz3r0-Nodes 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-30"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-30 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `be58f77d1cb0` · [字段定义](../../DATASET.md)*
