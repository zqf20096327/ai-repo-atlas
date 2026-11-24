# rafayshhh/p-pointer

⭐ 3 · Python · NOASSERTION · 推送 2026-11-21 · [GitHub](https://github.com/rafayshhh/p-pointer) · 个人维护

**用自然语言让 AI 代操作 Photoshop 的桌面代理**

一个自主桌面代理：接收用户自然语言指令，截取屏幕画面，调用 Gemini API 理解当前 Photoshop 界面，并通过 PyAutoGUI 模拟鼠标键盘操作完成图像编辑任务。项目以 Python 实现，实验性质、非官方，未与 Adobe 关联；用户需自备 Gemini API key 才能运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 多模态感知：截屏后由 Gemini 分析界面状态
- 通过 PyAutoGUI 执行 GUI 自动化操作
- 自然语言指令驱动 Photoshop 编辑流程

## 适用场景

- 让 AI 代替自己执行 Photoshop 中的重复性编辑步骤
- 通过文字描述生成设计修改而不手动操作菜单工具栏

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5: An autonomous desktop agent using the Gemini API to interact with creative tools.
> L8: - Experimental and unofficial.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 mid · 依据 README sha `9e97bb8b2db4` · [字段定义](../../DATASET.md)*
