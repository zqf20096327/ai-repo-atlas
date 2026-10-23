# pytorch/pytorch_sphinx_theme

⭐ 105 · CSS · MIT · 推送 2026-09-02 · [GitHub](https://github.com/pytorch/pytorch_sphinx_theme) · 组织维护

**PyTorch 文档与教程的 Sphinx 主题（已弃用维护）**

基于 Read the Docs Sphinx Theme 定制的 Sphinx 文档主题，用于渲染 PyTorch 官方文档与教程站点。开发流程：git clone 后 pip 安装为可编辑包，通过 yarn 或 npm 安装前端依赖，用 grunt 构建并支持 localhost:1919 实时预览；可在 conf.py 中将 html_theme 指向本地仓库对真实 Docs/Tutorials 仓库进行联调。README 明确声明该包不再积极维护，新贡献应转向 pytorch_sphinx_theme2 分支。

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

- 基于 Read the Docs Sphinx Theme 的定制 Sphinx 主题
- grunt 构建流程与实时预览（localhost:1919）
- 可对 pytorch/docs 与 tutorials 仓库做本地主题联调
- README 顶部声明弃用，后续转向 pytorch_sphinx_theme2

## 适用场景

- 为 PyTorch 类项目生成统一风格的 Sphinx 文档站
- 本地修改并预览 PyTorch 文档主题
- 参考主题结构定制自己的 Sphinx 主题

## 场景标签

 · 领域:开发工具/文档

## 证据(README 行号)

> L3: > ⚠️ **DEPRECATION NOTICE**: This package (`pytorch_sphinx_theme`) is no longer actively supported. We are now activ
> L5: Sphinx theme for PyTorch Docs and PyTorch Tutorials based on the Read the Docs Sphinx Theme.

## 星数曲线

```mermaid
xychart-beta
    title "pytorch/pytorch_sphinx_theme 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 104 --> 106
    line [105, 105]
```

2026-10-18 105 → 2026-10-23 105（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `74ae917088fe` · [字段定义](../../DATASET.md)*
