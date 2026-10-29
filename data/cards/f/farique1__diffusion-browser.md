# farique1/diffusion-browser

⭐ 43 · Python · 推送 2025-11-18 · [GitHub](https://github.com/farique1/diffusion-browser) · 个人维护

**查看 AI 生成图像及嵌入元数据的桌面浏览器**

基于 Pillow 的图像浏览工具，面向 Stable Diffusion（Automatic1111）、Fooocus、invoke-ai 等 AI 图像生成器的输出管理：读取图像内嵌元数据（prompt、seed、sampler、steps 等参数），建立本地数据库供后续检索，支持多文件夹与可选子文件夹递归、按参数搜索/排序/叠加显示、批量复制与信息导出。提供网格视图、全尺寸查看器与丰富的键盘快捷键，界面可通过 .ini 配置行列数、字体与配色。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 读取多种 AI 生成器（A1111/Fooocus/invoke-ai）内嵌元数据并解析参数
- 构建图像信息数据库，线程化加载图像
- 多路径与逐路径子文件夹递归配置
- 按参数搜索、精确匹配、排序与网格叠加显示

## 适用场景

- 浏览和检索本机 Stable Diffusion 生成的图像与其生成参数
- 按 seed、sampler 等参数筛选、排序大量生成图像
- 批量复制图像或导出元数据信息到文本文件

## 场景标签

 · 领域:AI 图像生成/媒体管理

## 证据(README 行号)

> L5: An easy way to view embedded image metadata of some AI generators.
> L213: prompt: infinite jest book cover
> L241: - Added support for Fooocus and Fooocus a1111 native embedded metadata

## 星数曲线

```mermaid
xychart-beta
    title "farique1/diffusion-browser 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-29 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `a8bf9ffc7627` · [字段定义](../../DATASET.md)*
