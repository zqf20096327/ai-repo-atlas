# anshk1234/molecule-visualiser

⭐ 24 · Python · MIT · 推送 2026-03-27 · [GitHub](https://github.com/anshk1234/molecule-visualiser) · [官网](https://atoms-molecule-visualiser.streamlit.app/) · 个人维护

**从 SMILES 生成分子 2D/3D 图标与可视化图标的工具**

读取 SMILES 化学结构式，按其拓扑生成分子图标，原子配色采用 CPK 惯例。提供三种使用方式：命令行脚本（支持 rdkit_svg 输出）、Python 解释器调用模块，以及 Streamlit Web 应用（另有在线部署可试用）。面向化学研究者和开发者，本地运行需克隆仓库并安装 packages.txt 中的 apt 依赖与 requirements.txt 的 pip 依赖。基于 RDKit 生成 SVG，代码以 MIT 许可发布，README 附 Zenodo DOI 引用信息。

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

- 按 SMILES 拓扑生成分子的 CPK 配色图标
- 提供命令行、Python 模块、Streamlit Web 三种使用方式
- 支持 rdkit_svg 输出与氢原子保留等选项

## 适用场景

- 为论文或课件批量生成分子结构图标
- 在 Web 界面交互式浏览分子结构
- 在 Python 脚本中程序化生成分子可视化图

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: Generate nice icons of molecules from SMILES.
> L59: python -m streamlit run streamlit_app.py

## 星数曲线

```mermaid
xychart-beta
    title "anshk1234/molecule-visualiser 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-26", "2026-10-30"]
    y-axis "stars" 21 --> 25
    line [22, 23, 24, 24]
```

2026-10-18 22 → 2026-10-30 24（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 low · 依据 README sha `f7ca2df467b9` · [字段定义](../../DATASET.md)*
