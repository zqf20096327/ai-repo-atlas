# highjive/nemo-workshop

⭐ 4 · Python · GPL-3.0 · 推送 2026-11-19 · [GitHub](https://github.com/highjive/nemo-workshop) · 个人维护

**本地离线运行的创意助手：硬件/故事/艺术等部门化创作**

完全在本机离线运行的创意助手，按部门组织：Workshop 把一句话需求转成硬件项目（零件清单、功耗预算、原理图、接线、3D 打印外壳与固件），Library 逐章写故事并配封面成书，另有 3D 建模、切片、Godot 小游戏、短片、有声书等部门。语言模型只在代码无法判断处填写内容，每步由代码检查。面向在普通电脑上离线创作的用户。当前为首个公开测试版，尚未在真实开发板上完成烧录验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 句子→硬件项目的八步流水线：零件、功耗、原理图、接线、外壳、固件
- 完全离线运行，声明不发送用户作品
- 语言模型 6.5 GB + 图像模型 2 GB，可在 8 GB 内存双核笔记本上运行
- NemoIso 提供 Debian 13 USB 启动镜像

## 适用场景

- 把一句话想法生成完整的 ESP32 硬件项目与固件
- 无网络环境下逐章创作故事并输出 PDF/Word 成书
- 在旧笔记本或 U 盘系统上离线运行创作工具

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L10: - **Workshop** turns a sentence ("a desk weather display with an OLED") into a
> L13:  step: the language model only fills in what code cannot decide, and code
> L23: Nemo is about helping people make things. It never sends your work anywhere.

## 星数曲线

```mermaid
xychart-beta
    title "highjive/nemo-workshop 星数(近 3 点)"
    x-axis ["2026-11-15", "2026-11-16", "2026-11-21"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-15 3 → 2026-11-21 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `0e03a17fedda` · [字段定义](../../DATASET.md)*
