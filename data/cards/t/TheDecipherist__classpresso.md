# TheDecipherist/classpresso

⭐ 78 · TypeScript · MIT · 推送 2026-06-17 · [GitHub](https://github.com/TheDecipherist/classpresso) · [官网](https://classpresso.com) · 个人维护

**构建后 CSS 工具类合并工具：压缩重复类名以加快渲染**

Classpresso 是一个在项目构建（npm run build）之后运行的 CLI 工具：扫描构建产物（.next/dist/build 等目录，自动检测），找出重复出现的工具类组合并合并为单个类，同时生成对应 CSS，从而减少浏览器样式计算与类查找工作量。声称样式重算快 50%、首次绘制快 42%。支持 Tailwind、Bootstrap、Bulma、Tachyons、UnoCSS 及 20+ 前端框架的构建输出；提供 analyze/optimize/validate/unused/report 子命令、SSR 水合安全模式与内容哈希重写。源代码不被修改，仅改写编译产物。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 构建后运行，扫描产物目录并合并重复工具类模式
- 支持 Tailwind/Bootstrap/UnoCSS 等 CSS 框架与 20+ 构建框架
- 提供 analyze/optimize/validate/unused/report 五个 CLI 子命令
- SSR 水合安全校验与内容哈希资源重命名（防缓存陈旧）

## 适用场景

- 减少大量工具类元素的浏览器样式重算开销
- 清理构建产物中未使用的 CSS 类
- 在 Next.js/Vite/Astro 等构建流程末尾追加优化步骤

## 场景标签

 · 领域:前端构建/性能优化

## 证据(README 行号)

> L7: Classpresso consolidates repeated utility class patterns at build time, dramatically reducing browser rendering work
> L77: npm install classpresso --save-dev

## 星数曲线

```mermaid
xychart-beta
    title "TheDecipherist/classpresso 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 77 --> 79
    line [78, 78]
```

2026-10-18 78 → 2026-10-29 78（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 low · 依据 README sha `516620788953` · [字段定义](../../DATASET.md)*
