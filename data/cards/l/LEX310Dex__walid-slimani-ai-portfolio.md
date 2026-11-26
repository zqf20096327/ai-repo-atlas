# LEX310Dex/walid-slimani-ai-portfolio

⭐ 8 · JavaScript · NOASSERTION · 推送 2026-11-22 · [GitHub](https://github.com/LEX310Dex/walid-slimani-ai-portfolio) · [官网](https://walid-slimani.vercel.app) · 个人维护

**AI/ML 工程师的交互式个人作品集网站**

Walid Slimani（ELTE 布达佩斯 AI 方向博士生）的个人作品集源码：纯静态站点，无框架无构建步骤，浏览器直接运行。前端机制包括自定义 GLSL 着色器驱动的 14,000 点 GPU 粒子形态变换（四种程序化点云）、GSAP ScrollTrigger 滚动编排、Web Audio 音效、SHA-256 清单校验的可复现部署（Vercel + GitHub Actions CI）。站点内容为 6 个 AI/ML 项目展示（逆设计、RL 路由、GNN 预测等），结果标注为简历与项目评估中报告的数值。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自定义 GLSL 着色器实现 GPU 粒子在四种点云间的形态变换
- prefers-reduced-motion、暂停动效控件与 Canvas/SVG 降级等无障碍处理
- 部署文件由 SHA-256 清单锁定，CI 校验完整性与语法
- 无框架无打包器，Three.js/GSAP 本地打包，无 CDN 运行时调用

## 适用场景

- 浏览作者在风电叶片、天线、MIMO 等领域的 AI 项目与报告结果
- 作为纯静态 WebGL 作品集站点的工程参考
- 本地克隆后用任意静态服务器直接预览站点

## 场景标签

 · 领域:个人网站/创意编程

## 证据(README 行号)

> L4: The interactive portfolio of an AI / ML engineer and AI PhD researcher at ELTE Budapest.
> L22: This repository is the source of my portfolio site. The site makes one point: **the domain changes, the method is A
> L93: |3D|Three.js r180 with custom `ShaderMaterial`; GLSL vertex and fragment shaders|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `7289ffaa6521` · [字段定义](../../DATASET.md)*
