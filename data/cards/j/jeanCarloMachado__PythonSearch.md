# jeanCarloMachado/PythonSearch

⭐ 14 · Python · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/jeanCarloMachado/PythonSearch) · 个人维护

**以 Python 代码存储条目的开发者生产力搜索引擎**

用 Python 字典收集命令、脚本、提示词、代码片段、URL 和文件等条目，通过终端 UI 或全局快捷键检索并执行，条目本身是代码因此可重构、复用和自动化。提供主 CLI（python_search 等一系列控制台脚本）和第二个前端：Rust 编写的 Spotlight 风格原生启动器 ps_ui，由常驻守护进程在内存中做模糊匹配与排序（约 0.1–2 ms），运行条目仍通过 run_key 调用 Python。支持 macOS 与 Linux，pip 安装主功能，Rust 前端需 cargo 1.82+ 自行构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 条目以 Python 字典存储，可检索、执行、重构与自动化
- Rust 原生启动器 ps_ui：常驻守护进程、内存内模糊匹配与排序
- 条目可绑定全局快捷键（macOS/GNOME/XFCE 统一定义）
- pip 安装附带约 14 个控制台脚本（CLI、剪贴板、通知、浏览器等）

## 适用场景

- 把常用命令、脚本和提示词集中管理并快速检索执行
- 通过全局快捷键直接打开 URL 或运行条目
- 像 Spotlight 一样用原生启动器快速调起工作流

## 场景标签

 · 领域:开发者工具/桌面效率

## 证据(README 行号)

> L3: Python search is a minimal search engine writting in python for developers productivity.
> L74: A resident daemon holds the entries in memory and ranks them in-process, so searching never starts

## 星数曲线

```mermaid
xychart-beta
    title "jeanCarloMachado/PythonSearch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 low · 依据 README sha `23c0ca93926a` · [字段定义](../../DATASET.md)*
