# LingyunStudio/AgnesStudio

⭐ 54 · Rust · MIT · 推送 2026-10-16 · [GitHub](https://github.com/LingyunStudio/AgnesStudio) · 组织维护 · 中文 README

**Agnes 图像/视频生成模型的 Windows 桌面客户端**

基于 Rust + Dioxus 构建的桌面客户端，为 Agnes AI 的图像与视频生成模型提供图形化操作界面：图像生成支持 Agnes Image 2.5/2.1/2.0 Flash 的文生图与图生图；视频生成支持 Agnes Video 2.5 Flash/2.5/V2.0，含首尾帧控制、参考图片与关键帧动画，异步任务自动轮询结果。使用需在设置中填写 Agnes API Key（Bearer Token），模型中 2.5 Flash 档位当前免费、部分模型付费。可执行文件约 8.4MB，面向 Windows 10/11，需 WebView2 运行时。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 图像生成：三个 Agnes Image 模型切换，文生图/图生图，档位式尺寸 1K–4K × 8 种宽高比
- 视频生成：Agnes Video 2.5 Flash/2.5/V2.0，支持首尾帧、图片/音频参考、关键帧动画
- 异步任务轮询与内嵌播放器预览，结果可保存为本地文件（MP4）
- 单文件 exe 分发（约 8.4MB），自动检查 GitHub Release 更新

## 适用场景

- 在桌面端通过图形界面使用 Agnes 模型生成图片
- 用文生视频/图生视频方式生成短视频并保存为 MP4
- 管理 API Key、保存目录与生成历史记录

## 场景标签

`图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L9:  AgnesStudio 是一款大小仅有不到 6MB，基于 Rust + Dioxus 构建的桌面客户端，为 Agnes AI 的图像与视频生成模型提供精美的图形化操作界面。
> L11: - 🖼 **图像生成**：支持 Agnes Image 2.5 / 2.1 / 2.0 Flash，文生图与图生图
> L12: - 🎬 **视频生成**：支持 Agnes Video 2.5 Flash / 2.5（文生视频、首尾帧、图片/音频/视频参考）与 V2.0（文生、图生、多图、关键帧动画）

## 星数曲线

```mermaid
xychart-beta
    title "LingyunStudio/AgnesStudio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 53 --> 55
    line [54, 54]
```

2026-10-18 54 → 2026-10-25 54（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `7479dbdba2e8` · [字段定义](../../DATASET.md)*
