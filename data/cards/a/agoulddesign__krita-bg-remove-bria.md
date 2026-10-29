# agoulddesign/krita-bg-remove-bria

⭐ 19 · Python · MIT · 推送 2026-03-31 · [GitHub](https://github.com/agoulddesign/krita-bg-remove-bria) · 个人维护

**Krita 插件：通过 BriaAI API 自动去除图层背景**

Krita 的 Python 插件，调用 BriaAI 的背景去除 API 处理选定图层，数秒内生成带 alpha 通道的新图层；支持批量模式并可调节并发线程数（默认等于处理器核心数）。安装需先注册 BriaAI 账号获取 API key（14 天免费试用，之后按次计费约 $0.018），插件经 Krita 的脚本导入功能装入并启用 Docker 面板。README 记录了使用限制：含透明通道的图层可能错位、不同尺寸图层可能异常、CMYK 等色彩空间可能出现色差；在 Krita 5.2.2/5.2.3/5.2.6 上测试，其他版本可能不兼容。2026 年 4 月注记称 BriaAI 已取消每月 1000 次免费额度，作者计划加入 ComfyUI 选项。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 调用 BriaAI API 对 Krita 图层做背景去除，生成带 alpha 通道的新图层
- 批量模式支持多图层处理，并发线程数可调（默认等于 CPU 核心数）
- 以 Krita Python 插件形式导入，通过 Docker 面板操作

## 适用场景

- 在 Krita 内直接给插画或照片抠出主体，无需切换到第三方应用
- 批量处理多个图层的背景去除
- 对去除结果不满意时将 alpha 转为透明度蒙版做进一步调整

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L7: ### A powerful Krita plugin for fast and automatic background removal using BriaAI's API.
> L32: 2. Click **Remove Background**. Processing may take a few seconds.

## 星数曲线

```mermaid
xychart-beta
    title "agoulddesign/krita-bg-remove-bria 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `bf62c4a54483` · [字段定义](../../DATASET.md)*
