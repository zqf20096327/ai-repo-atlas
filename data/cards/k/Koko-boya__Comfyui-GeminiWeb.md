# Koko-boya/Comfyui-GeminiWeb

⭐ 52 · Python · NOASSERTION · 推送 2026-03-18 · [GitHub](https://github.com/Koko-boya/Comfyui-GeminiWeb) · 个人维护

**让 ComfyUI 经 Gemini 网页接口生成/编辑图像的节点**

ComfyUI 自定义节点集，通过 Gemini 网页接口实现文生图、图生图与带图输入的对话（最多 5 张参考图），可选水印过滤。认证依赖浏览器 Cookie：支持手动粘贴、Cookie 文件与自动扫描浏览器（v20 App-Bound Encryption 解密仅测试 Edge 且需管理员运行）。依赖全部打包，无外部 API 包。README 声明按现状发布、无主动维护计划，并警告 Cookie 明文存储、关闭 SSL 校验，仅限本机私有环境使用。AGPL-3.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- text_to_image / image_to_image / chat 三种模式，最多 5 张参考图输入
- 三种 Cookie 认证方式：manual / cookie_file / auto_cookies
- 水印过滤选项（all / no_watermark / watermarked）
- 依赖自包含，内置 vendored Gemini-API 库

## 适用场景

- 在 ComfyUI 工作流里用 Gemini 网页版生成或编辑图像
- 以多张参考图做图像变换的节点式流水线
- 带图输入与 Gemini 进行视觉对话获取文本与思考过程

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: Custom ComfyUI nodes for **Google Gemini** image generation and editing using the Gemini web interface.
> L22: - **Text-to-Image** - Generate images from text using Gemini's native image model

## 星数曲线

```mermaid
xychart-beta
    title "Koko-boya/Comfyui-GeminiWeb 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-24 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `9b6cbed10f09` · [字段定义](../../DATASET.md)*
