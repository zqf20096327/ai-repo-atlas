# cosmiciron/layoutmaster

⭐ 44 · TypeScript · NOASSERTION · 推送 2026-06-20 · [GitHub](https://github.com/cosmiciron/layoutmaster) · [官网](https://layoutmaster.dev) · 个人维护

**浏览器内离线文本排版引擎：不依赖 DOM 直接计算布局**

面向前端开发者的 JavaScript 文本布局库：提供 form/fit/flow/pour 四个 API，在给定宽度、边界框、多区域或任意形状（exclusion 几何体，可由图像/视频 alpha 通道采样）内求解文本布局，返回精确坐标片段。内嵌基于 2D 空间模拟的布局引擎，无需 DOM 参与排版，包体约 243 kB（gzip 约 206 KiB）、零依赖，要求浏览器 Canvas API。通过 npm 安装，仓库附带多个浏览器 demo 与可复制的 helper 源码。README 未展示 AI 功能，'ai' 标签在本体中无对应实现描述。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- form/fit/flow/pour 四 API 覆盖定宽、溢出、多区域续排与任意形状填充
- exclusion 几何体可由图像/视频 alpha 通道采样，可序列化为 JSON 复用
- npm 包约 243 kB、零运行时依赖，需浏览器 Canvas API
- 提供 15 个浏览器 demo 与官方 helper 示例源码（npm run serve 本地运行）

## 适用场景

- 无限滚动或巨型瀑布流场景下避免 DOM 布局抖动
- 文字绕排动态视频/图像轮廓（如 dancing text 效果）
- 多栏杂志式分栏与跨区域文本续排

## 场景标签

 · 领域:前端/布局引擎

## 证据(README 行号)

> L70: Under its tiny browser API is a deterministic 2D spatial simulation engine for layout —
> L250: *Layoutmaster is specifically built for the browser so it requires the Canvas

## 星数曲线

```mermaid
xychart-beta
    title "cosmiciron/layoutmaster 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-30 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 low · 依据 README sha `13383ea1e9f6` · [字段定义](../../DATASET.md)*
