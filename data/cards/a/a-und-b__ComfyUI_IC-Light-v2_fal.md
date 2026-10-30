# a-und-b/ComfyUI_IC-Light-v2_fal

⭐ 44 · Python · MIT · 推送 2026-06-13 · [GitHub](https://github.com/a-und-b/ComfyUI_IC-Light-v2_fal) · 个人维护

**ComfyUI 节点：经 fal.ai API 调用 IC-Light V2 做图像重打光换背景**

面向 ComfyUI 用户的自定义节点，通过 fal.ai API 调用 lllyasviel 的 IC-Light V2 模型，实现按文字描述对照片重新打光并替换背景。支持原生 ComfyUI 蒙版输入、可调生成参数（seed、光照方向、高低分辨率降噪强度、CFG 等）、单次请求生成多张图。需预装 ComfyUI 并配置 fal.ai API key，可经 ComfyUI Manager 安装或手动 git clone 到 custom_nodes 目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于文字描述的重打光与背景替换
- 支持 ComfyUI 原生蒙版定位目标区域
- 可调光照方向（左/右/上/下）与高分辨率修复参数
- 单次请求生成多张变体图

## 适用场景

- 在 ComfyUI 工作流中给照片换光照和背景
- 结合蒙版只对指定区域重打光
- 批量生成多张光照变体用于选图

## 场景标签

`图像生成` `图像视频处理` · 领域:内容生成

## 证据(README 行号)

> L3: Custom node for ComfyUI that integrates lllyasviel's IC-Light V2 model into your workflows using the fal.ai API.
> L16: * ComfyUI installed and set up
> L17: * fal.ai account and API key

## 星数曲线

```mermaid
xychart-beta
    title "a-und-b/ComfyUI_IC-Light-v2_fal 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-30 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `f1c790c7e8b3` · [字段定义](../../DATASET.md)*
