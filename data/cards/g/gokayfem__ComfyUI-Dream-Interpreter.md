# gokayfem/ComfyUI-Dream-Interpreter

⭐ 86 · Python · Apache-2.0 · 推送 2026-08-01 · [GitHub](https://github.com/gokayfem/ComfyUI-Dream-Interpreter) · 个人维护

**ComfyUI 节点包：全景图校验修复、相机视图与梦境创作日志工具**

ComfyUI 自定义节点集合，围绕等距柱状全景图提供 2:1 几何校验与尺寸修复、接缝修复、透视相机视图、Little Planet 投影，以及交互式 360° WebGL 查看器；文本侧提供提示词构建、确定性主题标签提取与 Markdown/JSON 日志记录。投影与文本工具为确定性 CPU 操作，不依赖 CUDA/ROCm/MPS，无运行时网络请求，明确声明不构成心理或医学诊断。经 ComfyUI Manager 或手动克隆安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 等距柱状全景图校验、接缝修复与确定性投影节点
- 交互式 360° WebGL 查看器（本地 Three.js 资源、无 CDN、无遥测）
- 提示词构建、主题标签提取与 Markdown/JSON 日志记录
- 投影与文本工具为确定性 CPU 操作，独立于 CUDA/ROCm/MPS

## 适用场景

- 在 ComfyUI 工作流中校验并修复全景图
- 从全景图生成透视视图与 Little Planet 投影
- 以结构化日志记录创作笔记与主题标签

## 场景标签

`图像视频处理` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: An offline panorama, creative-reflection, and visual-journaling toolkit for ComfyUI. It validates and repairs equire
> L38: Restart ComfyUI. Nodes are under `visualization/3D` and `dream/panorama`.

## 星数曲线

```mermaid
xychart-beta
    title "gokayfem/ComfyUI-Dream-Interpreter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 85 --> 87
    line [86, 86]
```

2026-10-18 86 → 2026-10-25 86（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `deb7f6fe398b` · [字段定义](../../DATASET.md)*
