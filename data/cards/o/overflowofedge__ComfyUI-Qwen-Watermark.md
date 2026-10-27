# overflowofedge/ComfyUI-Qwen-Watermark

⭐ 25 · Python · MIT · 推送 2026-10-11 · [GitHub](https://github.com/overflowofedge/ComfyUI-Qwen-Watermark) · 个人维护 · 中文 README

**ComfyUI 去水印工作流：Qwen3-VL 检测、Qwen Image 2.1 局部修复**

一套在本机 ComfyUI 运行的水印/马赛克/不规则贴纸去除工作流与自定义节点插件（QWMDetect 等 6 个新节点）。Qwen3-VL 在一次推理中完成通用扫描与 Logo 复核，按遮挡类型选择矩形框或 SAM 生成遮罩，交由 Qwen Image 2.1 做局部修复，之后自动复检残留并可追加一次修复；选区外像素逐像素保护。提供 CLI 批处理、结构保护版本工作流与质量报告输出。模型权重不含在仓库中，需自备并按目录放置；建议 ComfyUI 0.38.2+，实测环境为 RTX 4060 Laptop 8GB。README 声明仅处理拥有版权或已授权的图片。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Qwen3-VL 检测 + 按类型选择 box/SAM 遮罩 + Qwen Image 2.1 局部修复
- 自动残留复检并最多追加一次局部修复，选区外像素逐像素保护
- 6 个自定义 ComfyUI 节点，含结构保护版本工作流与手动遮罩路径
- CLI 批处理支持断点续跑、质量报告与诊断输出

## 适用场景

- 去除自有图片上的文字、Logo、半透明水印
- 修复马赛克、色块与不规则贴纸遮挡（含人物结构保护）
- 批量处理图片目录并生成质量报告

## 场景标签

`图像生成` `图像视频处理` · 领域:内容生成

## 证据(README 行号)

> L5: 一套在本机 ComfyUI 运行的去水印工作流：Qwen3-VL 会在一次推理中完成通用扫描和 Logo 专项复核，自动识别文字、半透明 Logo、马赛克、矩形色块和不规则贴纸，再按类型选择矩形框或 SAM，交给 Qwen Imag
> L71: 建议使用 ComfyUI 0.38.2 或更新版本，并确认当前版本提供官方节点 `TextEncodeQwenImage21`、`QwenImage21Cache`。模型文件不包含在仓库或压缩包中，请按下表放置：

## 星数曲线

```mermaid
xychart-beta
    title "overflowofedge/ComfyUI-Qwen-Watermark 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-27 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `0378ccafb78b` · [字段定义](../../DATASET.md)*
