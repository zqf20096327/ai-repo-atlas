# amarnath3003/Solar-Roof-AI

⭐ 132 · TypeScript · 推送 2026-07-05 · [GitHub](https://github.com/amarnath3003/Solar-Roof-AI) · [官网](https://solar-roof-ai-frontend.vercel.app/) · 个人维护

**交互式太阳能屋顶规划工作台：AI 屋顶检测与排板估算**

面向太阳能规划的 Web 应用：在地图上搜索房产、手动或借助 AI 绘制屋顶与障碍物多边形，通过 Roboflow 托管工作流从卫星影像检测屋顶平面与障碍物，检测结果可预览、调置信度过滤后再应用；随后计算可用面积、叠加日照热力图、模拟手动或自动排板并实时计数容量，输出财务估算、GeoJSON 导出与蓝图式 PDF 报告。前端为 React 18 + Vite + TypeScript（Leaflet、Turf.js、Recharts），检测服务由浏览器直接调用 Roboflow serverless API。限制：结果用于规划与售前探索，非许可证级工程数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 地图优先工作区，手动绘制屋顶/障碍物图层，支持不规则形状与排除区
- 调用 Roboflow 托管工作流做屋顶平面与障碍物检测，结果可审核过滤后应用
- 面积计算、日照热力图与手动/自动排板模拟，含防重叠校验
- 财务估算仪表盘、GeoJSON 导出与蓝图式 PDF 报告生成

## 适用场景

- 太阳能安装商做屋顶可行性与排板的售前探索
- 在地图上评估屋顶可用面积与系统容量、财务回报
- 生成规划交接用的 PDF 报告与几何数据导出

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L4:  An interactive solar planning workspace for rooftop mapping, AI-assisted roof detection, panel layout simulation, a
> L51: ### 3️⃣ AI-Assisted Roof Detection

## 星数曲线

```mermaid
xychart-beta
    title "amarnath3003/Solar-Roof-AI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 131 --> 133
    line [132, 132]
```

2026-10-18 132 → 2026-10-29 132（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `468afda14a77` · [字段定义](../../DATASET.md)*
