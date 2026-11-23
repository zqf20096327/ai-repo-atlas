# shiquda/open-pptd-skill

⭐ 4 · Rust · MIT · 推送 2026-10-28 · [GitHub](https://github.com/shiquda/open-pptd-skill) · 个人维护 · 中文 README

**给 AI Coding Agent 与开发者的离线 PPT 编译技能与 Rust 编译器**

提供 SKILL.md 形式的 agent 技能与 `pptd` 原生 Rust CLI：用 YAML 编写 PPTD 工程描述幻灯片，编译为可编辑的原生 .pptx，也可将已有 PPTX 反编译回 PPTD。构建期零网络调用，二进制从固定 GitHub Release 下载并强制 SHA256 校验，校验失败回退到源码编译。支持 LaTeX 数学公式转原生 OOXML、矢量形状、双向表格、演讲者备注、1422 个内嵌 Font Awesome 图标；声明式图表语法与时序动画暂不支持，会被静态校验拦截。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YAML 声明式 PPTD 源码编译为原生可编辑 PPTX，并支持反向反编译
- LaTeX 数学公式编译为原生 OOXML 可编辑公式，不支持命令硬报错
- 毫秒级离线构建，零网络调用，二进制固定版本 + SHA256 校验
- 12 套真实文稿 / 98 页的回归验证套件与分层测试矩阵

## 适用场景

- 让 Codex/Claude 类 Coding Agent 按主题生成可二次编辑的 PPTX
- 内网离线环境下批量生成演示文稿
- 将已有 PPTX 反编译为 YAML 源码工程进行版本化管理

## 场景标签

 · 领域:开发者工具/文档生成

## 证据(README 行号)

> L5: **Open PPTD** 是面向 AI Coding Agent 与开发者的离线 PowerPoint / PPTX generator 和 agent skill：用 YAML 编写 PPTD，以原生 Rust 编译器生成可编辑
> L35: > - **② 运行时 = 原生 Rust 编译器 `pptd`**。真正的 PPTD → PPTX 编译由单文件原生 Rust 二进制完成（毫秒级、完全离线、构建期零 Node 依赖），由上一步的 `python3 …/inst

## 星数曲线

```mermaid
xychart-beta
    title "shiquda/open-pptd-skill 星数(近 3 点)"
    x-axis ["2026-11-02", "2026-11-21", "2026-11-23"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-02 3 → 2026-11-23 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `acc7a2e742c1` · [字段定义](../../DATASET.md)*
