# AviVahl/ts-tools

⭐ 170 · TypeScript · MIT · 推送 2026-10-24 · [GitHub](https://github.com/AviVahl/ts-tools) · 个人维护

**Node.js 下直接运行 TypeScript 源码的工具包集合**

面向 TypeScript/Node.js 开发者的工具包集合，含五个 npm 包：@ts-tools/node 通过 require.extensions 钩子让 CommonJS 环境直接执行 .ts/.tsx 源文件；@ts-tools/esm 提供 ESM loader 实现同样能力；@ts-tools/webpack-loader 是 webpack 的 TypeScript loader；@ts-tools/transpile 提供转译辅助函数；@ts-tools/robotrix 提供自定义 TypeScript 转译 transformers。整体 MIT 许可，README 未给出具体安装命令细节。仓库本身与 AI 无关，属于纯前端/Node 开发工具链。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- requireextensions 钩子使 CommonJS 直接执行 .ts/.tsx 源文件
- 提供 ESM loader 版本（@ts-tools/esm）
- webpack 专用 TypeScript loader
- 自定义 TypeScript 转译 transformers 集合

## 适用场景

- 在 Node.js 中免构建直接运行 TypeScript 源码
- 在 webpack 构建流程中处理 TypeScript 文件
- 编写自定义 TypeScript 转译变换器

## 场景标签

 · 领域:前端/Node.js 开发工具

## 证据(README 行号)

> L3: Several packages to assist TypeScript developers working with Node.js.
> L7: - **@ts-tools/node** - TypeScript support for Node.js. Registers a `require.extensions` (CommonJS) hook, allowing ex

## 星数曲线

```mermaid
xychart-beta
    title "AviVahl/ts-tools 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 169 --> 171
    line [170, 170]
```

2026-10-18 170 → 2026-10-24 170（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 low · 依据 README sha `be9437cbe617` · [字段定义](../../DATASET.md)*
